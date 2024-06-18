from flask import render_template, request, url_for, redirect, flash, send_file, abort,make_response
from flask import Blueprint
from flask_login import login_required, current_user
from ntb_marine import app_config, auth, __version__, app, ms_file_control, db
from ntb_marine.models import DocTemplate, FileCategory, Document, Ship
from flask_wtf import FlaskForm
from ntb_marine.document.forms import TemplateSearchForm, SignatureForm
from io import BytesIO
import datetime

document = Blueprint('document', __name__)

@document.route("/doc_temps", methods=["GET", "POST"])
@login_required
def doc_temps():
    template_search_form = TemplateSearchForm()
    signature_form = SignatureForm()
    page = request.args.get('page', 1, type=int)
    doc_templates = DocTemplate.query.order_by(DocTemplate.id.desc()).paginate(page=page, per_page=12)
    file_categories = FileCategory.query.order_by(FileCategory.id.asc()).all()
    # 船の一覧を取得
    ships = Ship.query.all()
    # 選択肢を設定
    signature_form.ship_id.choices = [(0, "船名を選択して下さい")] + [(ship.id, ship.name) for ship in ships]

    # if signature_form.validate_on_submit():
    #         template = DocTemplate.query.filter_by(id=signature_form.template_id.data).first_or_404()
    #         if template:
    #             document = Document(
    #                 doc_code=template.doc_code, name=template.name,
    #                 file_category_id=template.file_category_id, signature=signature_form.signature.data,
    #                 ship_id=signature_form.ship_id.data
    #             )
    #             db.session.add(document)
    #             db.session.commit()
    #             file_content, status_code = ms_file_control.download_file(template.file_id, auth, app_config)
    #             if status_code == 200:
    #                 file_name = f"ID_{document.id}_{datetime.datetime.now().strftime('%Y%m%d')}_{template.doc_code}.{template.file_name.split('.')[-1]}"
    #                 document.file_name = file_name
    #                 db.session.commit()
    #                 response = send_file(file_content, as_attachment=True, download_name=file_name)
    #                 return response
    #             else:
    #                 return abort(status_code)
    # else:
    #     print(signature_form.errors)

    return render_template('documents/template_list.html', signature_form=signature_form, ships=ships, doc_templates=doc_templates, file_categories=file_categories,template_search_form=template_search_form,current_user=current_user, version=__version__)

@document.route('/<int:file_category_id>/category_posts>')
@login_required
def category_posts(file_category_id):
    template_search_form = TemplateSearchForm()
    signature_form = SignatureForm()
    # 船の一覧を取得
    ships = Ship.query.all()
    # 選択肢を設定
    signature_form.ship_id.choices = [(0, "船名を選択して下さい")] + [(ship.id, ship.name) for ship in ships]
    # カテゴリ名を取得
    file_category = FileCategory.query.filter_by(id=file_category_id).first_or_404()

    # テンプレートの取得
    page = request.args.get('page', 1, type=int)
    doc_templates = DocTemplate.query.filter_by(file_category_id=file_category_id).order_by(DocTemplate.id.desc()).paginate(page=page, per_page=12)
    file_categories = FileCategory.query.order_by(FileCategory.id.asc()).all()
    return render_template('documents/template_list.html', signature_form=signature_form, ships=ships, doc_templates=doc_templates, file_categories=file_categories, file_category=file_category, template_search_form=template_search_form,current_user=current_user, version=__version__)

@document.route('/search', methods=['GET','POST'])
@login_required
def search():
    template_search_form = TemplateSearchForm()
    signature_form = SignatureForm()
    # 船の一覧を取得
    ships = Ship.query.all()
    # 選択肢を設定
    signature_form.ship_id.choices = [(0, "船名を選択して下さい")] + [(ship.id, ship.name) for ship in ships]
    searchtext = ""
    if template_search_form.validate_on_submit():
        searchtext = template_search_form.searchtext.data
    elif request.method == 'GET':
        template_search_form.searchtext.data = ""
#   ブログ記事の取得
    page = request.args.get('page', 1, type=int)
    if searchtext == "" or searchtext is None:
        doc_templates = DocTemplate.query.order_by(DocTemplate.id.desc()).paginate(page=page, per_page=12)
    else:    
        doc_templates = DocTemplate.query.filter((DocTemplate.doc_code.contains(searchtext)) | (DocTemplate.name.contains(searchtext)) | DocTemplate.file_name.contains(searchtext)).order_by(DocTemplate.id.desc()).paginate(page=page, per_page=12)
#   最新記事の取得
    # recent_blog_posts = BlogPost.query.order_by(BlogPost.id.desc()).limit(5).all()
#   カテゴリの取得
    file_categories = FileCategory.query.order_by(FileCategory.id.asc()).all()
    return render_template('documents/template_list.html', signature_form=signature_form, ships=ships, doc_templates=doc_templates, file_categories=file_categories, template_search_form=template_search_form,current_user=current_user, version=__version__)

@document.route('/<int:doc_template_id>/download')
@login_required
def download(doc_template_id):
    doc_template = DocTemplate.query.filter_by(id=doc_template_id).first_or_404()
    file_content, status = ms_file_control.download_file(doc_template.file_id, auth, app_config)
    if status!= 200:
        return  status
    return send_file(file_content, as_attachment=True, download_name=doc_template.file_name)

@document.route('/create_document', methods=['GET', 'POST'])
def create_document():
    signature_form = SignatureForm()
    # print("create_documentが起動しました")
    # 船の一覧を取得
    ships = Ship.query.all()
    # 選択肢を設定
    signature_form.ship_id.choices = [(0, "船名を選択して下さい")] + [(ship.id, ship.name) for ship in ships]

    if request.method == 'POST':
        # print("validate_on_submit()がtrue")
        # print(f"テンプレートID: {signature_form.template_id}")
        template = DocTemplate.query.filter_by(id=signature_form.template_id.data).first_or_404()
        if template:
            # print(f"テンプレートID: {signature_form.template_id.data}")
            document = Document(
                doc_code=template.doc_code, 
                name=template.name, 
                file_name = None, 
                file_id = None, 
                file_category_id=template.file_category_id, 
                signature=signature_form.signature.data, 
                ship_id=signature_form.ship_id.data)
            db.session.add(document)
            db.session.commit()  # Documentオブジェクトをデータベースに追加してコミット

            file_content, status_code = ms_file_control.download_file(template.file_id, auth, app_config)
            # print(f"ファイルID: {template.file_id}")
            if status_code == 200:
                file_extension = template.file_name.split('.')[-1]
                if file_extension == 'xlsx':
                    mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                elif file_extension == 'docx':
                    mime_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                elif file_extension == 'doc':
                    mime_type = 'application/msword'
                else:
                    mime_type = 'application/octet-stream'  # デフォルトのMIMEタイプ                # response = send_file(file_content, as_attachment=False, download_name=file_name)
                file_name = f"ID_{document.id}_{datetime.datetime.now().strftime('%Y%m%d')}_{template.doc_code}..{file_extension}"
                document.file_name = file_name  # Documentオブジェクトのfile_nameを更新
                db.session.commit()  # Documentオブジェクトを更新してコミット

                # send_fileを使用して適切なHTTPヘッダーを設定
                response = make_response(file_content.getvalue())
                response.headers.set('Content-Disposition', 'attachment', filename=file_name)
                response.headers.set('Content-Type', mime_type)
                return response
            else:
                return abort(status_code)
    return  redirect(url_for('document.doc_temps'))
# render_template('create_document.html', signature_form=signature_form, templates=templates)
# Gitにpush出来ないので、変更します。