from flask import render_template, request, url_for, redirect, flash, send_file, abort
from flask import Blueprint
from ntb_marine import app_config, auth, __version__, app
from ntb_marine import ms_file_control 
import requests

file_control = Blueprint('file_control', __name__)

@file_control.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if "file" not in request.files:
            flash("ファイルが選択されていません。")
            return redirect(request.url)
        
        file = request.files["file"]
        
        if file.filename == "":
            flash("ファイルが選択されていません。")
            return redirect(request.url)

        if file:
            result = ms_file_control.upload_file_to_sharepoint(file, auth, app_config)
            if result:
                flash("ファイルが正常にアップロードされました。")
            else:
                flash("ファイルのアップロードに失敗しました。")
            return redirect(url_for("logins.index"))
    return render_template("file_control/upload.html", username=auth.get_user()["name"])

@file_control.route("/list_files", methods=["GET"])
@file_control.route("/list_files/<folder_id>", methods=["GET"])
def list_files(folder_id=None):
    files, folders, file_ids, folder_ids, status = ms_file_control.list_files(auth, folder_id, app_config)
    if status!= 200:
        return  status
    return render_template("file_control/file_list.html", files=files, folders=folders)

@file_control.route("/download/<file_id>/<file_name>", methods=["GET"])
def download_file(file_id, file_name):
    file_content, status = ms_file_control.download_file(file_id, auth, app_config)
    if status!= 200:
        return  status
    return send_file(file_content, as_attachment=True, download_name=file_name)

@file_control.route("/create_folder", methods=["POST","GET"])
def create_folder():
    folder_name = request.form.get("folder_name")
    if not folder_name:
        return render_template('file_control/create_folder.html')
    folder_id, status = ms_file_control.create_folder(folder_name, auth, app_config)
    if status not in [200, 201]:
        flash("error: Could not create folder")
        return redirect(url_for("logins.index"))
    
    flash(f"フォルダが正常に作成されました。フォルダID: {folder_id}")
    return redirect(url_for("file_control.upload_to_folder_page", folder_id=folder_id))

@file_control.route("/upload_to_folder_page/<folder_id>", methods=["GET", "POST"])
def upload_to_folder_page(folder_id):
    if request.method == "POST":
        if "file" not in request.files:
            flash("ファイルが選択されていません。")
            return redirect(request.url)
        
        file = request.files["file"]
        
        if file.filename == "":
            flash("ファイルが選択されていません。")
            return redirect(request.url)

        if file:
            result = ms_file_control.upload_file_to_specific_folder(file, folder_id, auth, app_config)
            if result:
                flash("ファイルが正常にアップロードされました。")
            else:
                flash("ファイルのアップロードに失敗しました。")
            return redirect(url_for("logins.index"))
    return render_template("file_control/upload_to_folder.html", folder_id=folder_id)

