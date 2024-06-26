from flask import render_template, request, url_for, redirect, flash, send_file, abort,send_from_directory,session
from flask import Blueprint
from flask_login import login_required, current_user
from ntb_marine import app_config, auth, __version__, app, ms_file_control, db
from ntb_marine.models import DocTemplate, FileCategory, Document, Ship
from flask_wtf import FlaskForm
from ntb_marine.document.forms import TemplateSearchForm, SignatureForm,EditedSearchForm,EditedSignatureForm
from io import BytesIO
from os.path import normpath
from datetime import datetime
from tempfile import gettempdir
import os 
import functools
from sqlalchemy.sql import or_
import mimetypes
from pytz import timezone

document = Blueprint('document', __name__)

# カスタムフィルタを定義
@app.template_filter('format_datetime')
def format_datetime(value):
    if value is None:
        return ""
    # 日付を "年-月-日" 形式にフォーマット
    return value.strftime('%Y年%m月%d日')

# アプリケーションにフィルタを登録
app.jinja_env.filters['format_datetime'] = format_datetime
#設置方法： <p class="card-text">日付:{{ edited.updated_at | format_datetime  }}</p>

def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not auth.get_user():
            return redirect(url_for("logins.login", next=request.path))
        return func(*args, **kwargs)
    return wrapper
def get_common_data():
    template_search_form = TemplateSearchForm()
    signature_form = SignatureForm()
    # 船の一覧を取得
    ships = Ship.query.all()
    edited_docs = Document.query.filter(Document.file_id.is_not(None)).order_by(Document.updated_at.desc()).limit(5).all()
    # 選択肢を設定
    signature_form.ship_id.choices = [(0, "船名を選択して下さい")] + [(ship.id, ship.name) for ship in ships]
    file_categories = FileCategory.query.order_by(FileCategory.id.asc()).all()
    return {
        'template_search_form': template_search_form,
        'signature_form': signature_form,
        'ships': ships,
        'edited_docs': edited_docs,
        'file_categories': file_categories,
        'current_user': current_user,
        'version': __version__
    }

@document.route("/doc_temps", methods=["GET", "POST"])
@login_required
def doc_temps():
    common_data = get_common_data()
    # paginateの記述    
    page = request.args.get('page', 1, type=int)
    doc_templates = DocTemplate.query.order_by(DocTemplate.id.desc()).paginate(page=page, per_page=12)

    return render_template('documents/template_list.html', **common_data, doc_templates=doc_templates)

@document.route('/<int:file_category_id>/category_posts>')
@login_required
def category_posts(file_category_id):
    common_data = get_common_data()
    # カテゴリ名を取得
    file_category = FileCategory.query.filter_by(id=file_category_id).first_or_404()
    common_data['file_category'] = file_category
    # paginateの記述    
    page = request.args.get('page', 1, type=int)
    # テンプレートの取得
    doc_templates = DocTemplate.query.filter_by(file_category_id=file_category_id).order_by(DocTemplate.id.desc()).paginate(page=page, per_page=12)
    return render_template('documents/template_list.html', **common_data, doc_templates=doc_templates)

@document.route('/search', methods=['GET','POST'])
@login_required
def search():
    common_data = get_common_data()
    searchtext = ""
    if common_data['template_search_form'].validate_on_submit():
        searchtext = common_data['template_search_form'].searchtext.data
    elif request.method == 'GET':
        common_data['template_search_form'].searchtext.data = ""
    # テンプレートの取得
    page = request.args.get('page', 1, type=int)
    if searchtext == "" or searchtext is None:
        doc_templates = DocTemplate.query.order_by(DocTemplate.id.desc()).paginate(page=page, per_page=12)
    else:    
        doc_templates = DocTemplate.query.filter((DocTemplate.doc_code.contains(searchtext)) | (DocTemplate.name.contains(searchtext)) | DocTemplate.file_name.contains(searchtext)).order_by(DocTemplate.id.desc()).paginate(page=page, per_page=12)
    return render_template('documents/template_list.html', **common_data, doc_templates=doc_templates)

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
@login_required
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
                mime_type = mimetypes.guess_type(template.file_name)[0] or 'application/octet-stream'
                file_extension = template.file_name.split('.')[-1]
                file_name = f"ID_{document.id}_{document.ship_id}_{datetime.now().strftime('%Y%m%d')}_{template.doc_code}.{file_extension}"
                document.file_name = file_name  # Documentオブジェクトのfile_nameを更新
                db.session.commit()  # Documentオブジェクトを更新してコミット
                session['file_name'] = file_name
                return send_file(
                    file_content,
                    mimetype=mime_type,
                    as_attachment=True,
                    download_name=file_name
                )            
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
        common_data = get_common_data()
        page = request.args.get('page', 1, type=int)
        doc_templates = DocTemplate.query.order_by(DocTemplate.id.desc()).paginate(page=page, per_page=12)
        edited_list = Document.query.filter(Document.file_id.is_not(None)).order_by(Document.updated_at.desc()).paginate(page=page, per_page=12)
        template_name = request.args.get('template', 'template_list')
        if template_name == 'edited_list':
            edited_form = EditedSearchForm()
            Editedsignature_form = EditedSignatureForm()
            context = {
                **common_data,
                'edited_list': edited_list,
                'edited_form': edited_form,
                'edited_signature_form':Editedsignature_form
            }
            template_file = 'documents/edited_list.html'
        elif template_name == 'template_list':
            context = {
                **common_data,
                'doc_templates': doc_templates
            }
            template_file = 'documents/template_list.html'
        temp_file_path = session.get('temp_file_path')
        document_id =  session.get('document_id')
        document = Document.query.filter_by(id=document_id).first_or_404()
        # print('>>>5')
        file_name = os.path.basename(temp_file_path)
        with open(temp_file_path, 'rb') as file:
            file_content = file.read()
            file_id, status_code = ms_file_control.upload_edited_files(file_content, file_name, auth, app_config)
        # SharePointにファイルをアップロード
        document.file_id = file_id
        db.session.commit()
        if status_code in [200, 201]:
            flash("ファイルが正常にアップロードされました。")
        else:
            flash(f"ファイルのアップロードに失敗しました。{status_code}")
            return redirect(url_for('document.upload_temp_file', template=template_name))  # Post/Redirect/Get パターンを使用
        # print(f'ここは？ file_id:{file_id}')    
        return render_template(template_file, **context)
    except Exception as e:
        print(f"Error in upload_temp_file: {e}")
        return 500

def id_of_document(file_name):
    # ID_ と _ の間の数字を取得
    id_part = file_name.split("ID_")[1].split("_")[0]
    # 数字を整数型に変換して返す
    return int(id_part)
# 手動でのファイルUpload
@document.route("/select_upload", methods=["GET", "POST"])
def select_upload():
    common_data = get_common_data()
    page = request.args.get('page', 1, type=int)
    doc_templates = DocTemplate.query.order_by(DocTemplate.id.desc()).paginate(page=page, per_page=12)
    edited_list = Document.query.filter(Document.file_id.is_not(None)).order_by(Document.updated_at.desc()).paginate(page=page, per_page=12)
    template_name = request.args.get('template', 'template_list')
    print(f"Template Name: {template_name}")
    if template_name == 'edited_list':
        edited_form = EditedSearchForm()
        Editedsignature_form = EditedSignatureForm()
        context = {
            **common_data,
            'edited_list': edited_list,
            'edited_form': edited_form,
            'Editedsignature_form':Editedsignature_form
        }
        template_file = 'documents/edited_list.html'
    elif template_name == 'template_list':
        context = {
            **common_data,
            'doc_templates': doc_templates
        }
        template_file = 'documents/template_list.html'
    if request.method == "POST":
        if "file" not in request.files:
            flash("ファイルが選択されていません。")
            return redirect(request.url)
        
        file = request.files["file"]
        file_name = file.filename
        file_content = file.read()
        if file.filename == "":
            flash("ファイルが選択されていません。")
            return redirect(request.url)
        try:
            document_id = id_of_document(file_name)
        except ValueError as e:
            flash(f"このファイルはアップロードできません。: {e}")
            return redirect(request.url)
        
        document = Document.query.filter_by(id=document_id).first()
        if document is None:
            flash("このドキュメントが見つかりません。選択したファイルはデータがありませんでした。")
            return redirect(request.url)
        if file:
            file_id, status_code = ms_file_control.upload_edited_files(file_content, file_name, auth, app_config)
            if status_code in [200, 201]:
                document.file_id = None
                db.session.commit()
                document.file_id = file_id
                # print(f'file_id:{file_id}')
                updateat =datetime.now(timezone('Asia/Tokyo'))
                print(f'更新日:{updateat}')
                db.session.commit()
                flash(f"ファイルが正常にアップロードされました。{status_code}")
                return redirect(url_for('document.select_upload', template=template_name))  # Post/Redirect/Get パターンを使用
            else:
                flash(f"ファイルのアップロードに失敗しました。{status_code}")
                return redirect(request.url)
    return render_template(template_file, **context)

@document.route("/edited_list", methods=["GET", "POST"])
@login_required
def edited_list():
    edited_form = EditedSearchForm() 
    Editedsignature_form = EditedSignatureForm()   
    common_data = get_common_data()
    page = request.args.get('page', 1, type=int)
    edited_list = Document.query.filter(Document.file_id.is_not(None)).order_by(Document.updated_at.desc()).paginate(page=page, per_page=12)
    return render_template('documents/edited_list.html', **common_data, edited_list=edited_list, edited_form=edited_form,Editedsignature_form=Editedsignature_form)

@document.route("/edited_serch", methods=["GET", "POST"])
@login_required
def edited_serch():
    common_data = get_common_data()
    edited_form = EditedSearchForm() 
    Editedsignature_form = EditedSignatureForm() 
    page = request.args.get('page', 1, type=int)
    searchdate = None  
    searchtext = None 
    if edited_form.validate_on_submit():
        searchtext = edited_form.searchtext.data
        searchdate_str = edited_form.searchdate.data
        if searchdate_str:
            try:
                searchdate = datetime.strptime(searchdate_str, '%Y-%m')
            except ValueError:
                flash('無効な日付形式です。正しい形式で入力してください。例: 2024-06', 'error')
                return redirect(request.url)

    elif request.method == 'GET':
        edited_form.searchtext.data = ""
        edited_form.searchdate.data = None

    if searchdate is None or searchdate == "":
        if searchtext == "" or searchtext is None:
            edited_list = Document.query.filter(Document.file_id.is_not(None)).order_by(Document.updated_at.desc()).paginate(page=page, per_page=12)
        else:    
            edited_list = Document.query.filter(Document.file_id.is_not(None))\
            .filter(or_(Document.doc_code.contains(searchtext), Document.name.contains(searchtext), Document.file_name.contains(searchtext)))\
            .order_by(Document.updated_at.desc()).paginate(page=page, per_page=12)
    else:
        serch_year = searchdate.year
        serch_month = searchdate.month
        start_date = datetime(serch_year, serch_month, 1)
        end_date = datetime(serch_year, serch_month + 1, 1)
        if searchtext == "" or searchtext is None:
            edited_list = Document.query.filter(Document.file_id.is_not(None))\
            .filter(Document.updated_at >= start_date, Document.updated_at < end_date)\
            .order_by(Document.updated_at.desc()).paginate(page=page, per_page=12)
        else:    
            edited_list = Document.query.filter(Document.file_id.is_not(None))\
            .filter(or_(Document.doc_code.contains(searchtext), Document.name.contains(searchtext), Document.file_name.contains(searchtext)))\
            .filter(Document.updated_at >= start_date, Document.updated_at < end_date)\
            .order_by(Document.updated_at.desc()).paginate(page=page, per_page=12)
    return render_template('documents/edited_list.html', **common_data, edited_list=edited_list,edited_form=edited_form,Editedsignature_form=Editedsignature_form)

@document.route('/<int:file_category_id>/edited_categories')
@login_required
def edited_categories(file_category_id):
    common_data = get_common_data()
    edited_form = EditedSearchForm()
    Editedsignature_form = EditedSignatureForm() 
    # カテゴリ名を取得
    file_category = FileCategory.query.filter_by(id=file_category_id).first_or_404()
    common_data['file_category'] = file_category
    # paginateの記述    
    page = request.args.get('page', 1, type=int)
    # テンプレートの取得
    edited_list = Document.query.filter(Document.file_id.is_not(None)).filter_by(file_category_id=file_category_id).order_by(Document.updated_at.desc()).paginate(page=page, per_page=12)
    return render_template('documents/edited_list.html', **common_data,  edited_list=edited_list,edited_form=edited_form,Editedsignature_form=Editedsignature_form)

@document.route('/edited_download', methods=['GET', 'POST'])
@login_required
def edited_download():
    Editedsignature_form = EditedSignatureForm()
    document = Document.query.filter_by(id=Editedsignature_form.document_id.data).first_or_404()
    file_name = document.file_name
    file_content, status = ms_file_control.download_file(document.file_id, auth, app_config)
    if status != 200:
        return status
    # ファイルのMIME型を取得
    mime_type = mimetypes.guess_type(file_name)[0] or 'application/octet-stream'
    # send_file関数を使用してファイルをダウンロード
    home_dir = os.path.expanduser("~")
    download_folder = os.path.join(home_dir, 'Downloads')
    download_file_path = os.path.join(download_folder, file_name)
    
    # ダウンロードしたファイル名&パスをsessionに代入
    session['temp_file_path'] = download_file_path
    session['document_id'] = document.id
    return send_file(
        file_content,
        as_attachment = True, 
        download_name=file_name,  
        mimetype=mime_type,
    )
# ダウンロードのテスト用
# @document.route('/make_response', methods=['GET', 'POST'])
# @login_required
# def make_response():
#     signature_form = SignatureForm()
#     ships = Ship.query.all()
#     signature_form.ship_id.choices = [(0, "船名を選択して下さい")] + [(ship.id, ship.name) for ship in ships]
 
#     if request.method == 'POST':
#         template = DocTemplate.query.filter_by(id=signature_form.template_id.data).first_or_404()

#         file_content, status_code = ms_file_control.download_file(template.file_id, auth, app_config)
#         if status_code == 200:
#             mime_type = mimetypes.guess_type(template.file_name)[0] or 'application/octet-stream'
#             file_extension = template.file_name.split('.')[-1]
#             file_name = f"ID_{datetime.now().strftime('%Y%m%d')}_{template.doc_code}.{file_extension}"
            
#     return send_file(
#         file_content,
#         mimetype=mime_type,
#         as_attachment=True,
#         download_name=file_name
#     )