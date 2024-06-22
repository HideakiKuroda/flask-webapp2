import requests

def user_info(auth, app_config=None):
    token_response = auth.get_token_for_user(app_config.SCOPE)
    if not token_response:
        return None, 401

    headers = {
        'Authorization': 'Bearer ' + token_response['access_token'],
        'Accept': 'application/json'
    }

    endpoint = "https://graph.microsoft.com/v1.0/me"
    
    response = requests.get(endpoint, headers=headers)
    user_info = response.json()

    return user_info    


from flask import render_template, request, send_file
from io import BytesIO
from ntb_marine import app, db
from models import Document, DocTemplate
from ntb_marine.document.forms import SignatureForm
from ntb_marine import ms_file_control, auth, app_config
import datetime

@app.route('/create_document', methods=['GET', 'POST'])
def create_document():
    form = SignatureForm()
    templates = DocTemplate.query.all()

    if request.method == 'POST' and form.validate_on_submit():
        template = DocTemplate.query.filter_by(id=form.id.data).first()
        if template:

            document = Document(doc_code=template.doc_code, name=template.name, file_category_id=template.file_category_id, signature=form.searchtext.data, ship_id=form.ship_id.data)
            db.session.add(document)
            db.session.commit()  # Documentオブジェクトをデータベースに追加してコミット

            file_content, status_code = ms_file_control.download_file(template.file_id, auth, app_config)
            if status_code == 200:
                file_name = f"ID_{document.id}_{datetime.datetime.now().strftime('%Y%m%d')}_{template.doc_code}.{template.file_name.split('.')[-1]}"
                document.file_name = file_name  # Documentオブジェクトのfile_nameを更新
                db.session.commit()  # Documentオブジェクトを更新してコミット

                response = send_file(file_content, as_attachment=True, download_name=file_name)
                return response

    return render_template('create_document.html', form=form, templates=templates)



@app.route('/create_document', methods=['GET', 'POST'])
def create_document():
    form = SignatureForm()
    templates = Template.query.all()

    if request.method == 'POST' and form.validate_on_submit():
        template = Template.query.filter_by(doc_code=form.doc_code.data).first()
        if template:
            auth = get_auth()
            app_config = get_app_config()

            document = Document(doc_code=template.doc_code, name=template.name, file_category_id=template.file_category_id, signature=form.searchtext.data, ship_id=form.ship_id.data)
            db.session.add(document)
            db.session.commit()  # Documentオブジェクトをデータベースに追加してコミット

            file_content, status_code = download_file(template.file_id, auth, app_config)
            if status_code == 200:
                file_name = f"ID_{document.id}_{form.searchtext.data}_{datetime.datetime.now().strftime('%Y%m%d')}_{template.doc_code}.{template.file_name.split('.')[-1]}"
                document.file_name = file_name  # Documentオブジェクトのfile_nameを更新
                db.session.commit()  # Documentオブジェクトを更新してコミット

                response = send_file(file_content, as_attachment=True, download_name=file_name)
                return response

    return render_template('create_document.html', form=form, templates=templates)
