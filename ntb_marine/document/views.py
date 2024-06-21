from flask import render_template, request, url_for, redirect, flash, send_file, abort,make_response,send_from_directory,session
from flask import Blueprint
from flask_login import login_required, current_user
from ntb_marine import app_config, auth, __version__, app, ms_file_control, db
from ntb_marine.models import DocTemplate, FileCategory, Document, Ship
from flask_wtf import FlaskForm
from ntb_marine.document.forms import TemplateSearchForm, SignatureForm
from io import BytesIO
from os.path import normpath
import datetime
from tempfile import gettempdir
import os 

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
    edited_docs = Document.query.filter(Document.file_id.is_not(None)).order_by(Document.updated_at.desc()).limit(5).all()
    # 選択肢を設定
    signature_form.ship_id.choices = [(0, "船名を選択して下さい")] + [(ship.id, ship.name) for ship in ships]

    return render_template('documents/template_list.html', edited_docs= edited_docs, signature_form=signature_form, ships=ships, doc_templates=doc_templates, file_categories=file_categories,template_search_form=template_search_form,current_user=current_user, version=__version__)

@document.route('/<int:file_category_id>/category_posts>')
@login_required
def category_posts(file_category_id):
    template_search_form = TemplateSearchForm()
    signature_form = SignatureForm()
    # 船の一覧を取得
    ships = Ship.query.all()
    edited_docs = Document.query.filter(Document.file_id.is_not(None)).order_by(Document.updated_at.desc()).limit(5).all()
    # 選択肢を設定
    signature_form.ship_id.choices = [(0, "船名を選択して下さい")] + [(ship.id, ship.name) for ship in ships]
    # カテゴリ名を取得
    file_category = FileCategory.query.filter_by(id=file_category_id).first_or_404()

    # テンプレートの取得
    page = request.args.get('page', 1, type=int)
    doc_templates = DocTemplate.query.filter_by(file_category_id=file_category_id).order_by(DocTemplate.id.desc()).paginate(page=page, per_page=12)
    file_categories = FileCategory.query.order_by(FileCategory.id.asc()).all()
    return render_template('documents/template_list.html', edited_docs= edited_docs, signature_form=signature_form, ships=ships, doc_templates=doc_templates, file_categories=file_categories, file_category=file_category, template_search_form=template_search_form,current_user=current_user, version=__version__)

@document.route('/search', methods=['GET','POST'])
@login_required
def search():
    template_search_form = TemplateSearchForm()
    signature_form = SignatureForm()
    # 船の一覧を取得
    edited_docs = Document.query.filter(Document.file_id.is_not(None)).order_by(Document.updated_at.desc()).limit(5).all()
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
    return render_template('documents/template_list.html', edited_docs= edited_docs, signature_form=signature_form, ships=ships, doc_templates=doc_templates, file_categories=file_categories, template_search_form=template_search_form,current_user=current_user, version=__version__)

@document.route('/<int:doc_template_id>/download')
@login_required
def download(doc_template_id):
    doc_template = DocTemplate.query.filter_by(id=doc_template_id).first_or_404()
    file_name = doc_template.name
    file_content, status = ms_file_control.download_file(doc_template.file_id, auth, app_config)
    if status != 200:
        return status
    # 一時的なファイルを作成して保存
    temp_folder = gettempdir()
    temp_file_path = os.path.join(temp_folder, file_name)
    with open(temp_file_path, 'wb') as f:
        f.write(file_content.getvalue())

    # send_from_directory関数を使用してファイルをダウンロード
    return send_from_directory(temp_folder, file_name, as_attachment=True)


@document.route('/create_document', methods=['GET', 'POST'])
def create_document():
    signature_form = SignatureForm()
    ships = Ship.query.all()
    signature_form.ship_id.choices = [(0, "船名を選択して下さい")] + [(ship.id, ship.name) for ship in ships]

    if request.method == 'POST':
        template = DocTemplate.query.filter_by(id=signature_form.template_id.data).first_or_404()
        if template:
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
            if status_code == 200:
                file_extension = template.file_name.split('.')[-1]
                file_name = f"ID_{document.id}_{document.ship_id}_{datetime.datetime.now().strftime('%Y%m%d')}_{template.doc_code}.{file_extension}"
                document.file_name = file_name  # Documentオブジェクトのfile_nameを更新
                db.session.commit()  # Documentオブジェクトを更新してコミット
                # PCのダウンロードフォルダとファイル名をつなげてdownload_file_path　アップロード時に必要
                home_dir = os.path.expanduser("~")
                download_folder = os.path.join(home_dir, 'Downloads')
                download_file_path = os.path.join(download_folder, file_name)
                
                temp_folder = gettempdir()
                temp_file_path = os.path.join(temp_folder, file_name)
                with open(temp_file_path, 'wb') as f:
                    f.write(file_content.getvalue())
                # ダウンロードしたファイル名&パスをsessionに代入
                session['temp_file_path'] = download_file_path
                session['document_id'] = document.id
                return send_from_directory(temp_folder, file_name, as_attachment=True)
            else:
                return abort(status_code)
    return status_code
# render_template('create_document.html', signature_form=signature_form, templates=templates)
# Gitにpush出来ないので、変更します。
# exfilename = session.get('filename')
# session['date'] = request.form['date']

@document.route("/upload_temp_file", methods=["POST"])
def upload_temp_file():
    try:
        # 一時的なファイルを読み込む
        temp_file_path = session.get('temp_file_path')
        document_id =  session.get('document_id')
        form_data = request.form.to_dict()  # request.formを辞書型に変換する
        form_data["temp_file_path"] = temp_file_path
        form_data["document_id"] = document_id
        # signature_form = SignatureForm(form_data=form_data)
        document = Document.query.filter_by(id=document_id).first_or_404()
        # print('>>>5')
        file_name = os.path.basename(temp_file_path)
        with open(temp_file_path, 'rb') as file:
            file_content = file.read()
            file_id, status_code = ms_file_control.upload_edited_files(file_content, file_name, auth, app_config)
        # SharePointにファイルをアップロード
        document.file_id = file_id
        db.session.commit()
        if status_code == 201:
            # flash("ファイルが正常にアップロードされました。")
            response = {"message": "ファイルが正常にアップロードされました。"}
        else:
            # flash(f"ファイルのアップロードに失敗しました。{status_code}")
            response = {"message": f"ファイルのアップロードに失敗しました。{status_code}"}
        # print(f'ここは？ file_id:{file_id}')    
        return response
    except Exception as e:
        print(f"Error in upload_temp_file: {e}")
        return 500
