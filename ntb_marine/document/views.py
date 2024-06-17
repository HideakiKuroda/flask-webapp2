from flask import render_template, request, url_for, redirect, flash, send_file, abort
from flask import Blueprint
from flask_login import login_required, current_user
from ntb_marine import app_config, auth, __version__, app, ms_file_control, db
from ntb_marine.models import DocTemplate, FileCategory, Document, Ship
from flask_wtf import FlaskForm
from ntb_marine.document.forms import TemplateSearchForm, SignatureForm
from io import BytesIO
import datetime

document = Blueprint('document', __name__)

@document.route("/doc_templs", methods=["GET", "POST"])
@login_required
def doc_temps():
    form = TemplateSearchForm()
    page = request.args.get('page', 1, type=int)
    doc_templates = DocTemplate.query.order_by(DocTemplate.id.desc()).paginate(page=page, per_page=12)
    file_categories = FileCategory.query.order_by(FileCategory.id.asc()).all()
    ships = Ship.query.all()

    return render_template('documents/template_list.html', doc_templates=doc_templates, file_categories=file_categories,form=form,current_user=current_user, version=__version__)

@document.route('/<int:file_category_id>/category_posts>')
@login_required
def category_posts(file_category_id):
    form = TemplateSearchForm()
    # カテゴリ名を取得
    file_category = FileCategory.query.filter_by(id=file_category_id).first_or_404()

    # テンプレートの取得
    page = request.args.get('page', 1, type=int)
    doc_templates = DocTemplate.query.filter_by(file_category_id=file_category_id).order_by(DocTemplate.id.desc()).paginate(page=page, per_page=12)
    file_categories = FileCategory.query.order_by(FileCategory.id.asc()).all()
    return render_template('documents/template_list.html', doc_templates=doc_templates, file_categories=file_categories, file_category=file_category, form=form,current_user=current_user, version=__version__)

@document.route('/search', methods=['GET','POST'])
@login_required
def search():
    form = TemplateSearchForm()
    searchtext = ""
    if form.validate_on_submit():
        searchtext = form.searchtext.data
    elif request.method == 'GET':
        form.searchtext.data = ""
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
    return render_template('documents/template_list.html', doc_templates=doc_templates, file_categories=file_categories, form=form,current_user=current_user, version=__version__)

@document.route('/<int:doc_template_id>/download')
@login_required
def download(doc_template_id):
    doc_template = DocTemplate.query.filter_by(id=doc_template_id).first_or_404()
    file_content, status = ms_file_control.download_file(doc_template.file_id, auth, app_config)
    if status!= 200:
        return  status
    return send_file(file_content, as_attachment=True, download_name=doc_template.file_name)

@app.route('/create_document', methods=['GET', 'POST'])
def create_document():
    form = SignatureForm()
    templates = DocTemplate.query.all()
    ships = Ship.query.all()

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

