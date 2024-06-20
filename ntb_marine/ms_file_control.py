import requests
from flask import flash, redirect, url_for
from io import BytesIO
import re

def upload_file_to_sharepoint(file, auth, app_config):
    try:
        token_response = auth.get_token_for_user(app_config.SCOPE)
        if not token_response:
            return None, 401

        headers = {
            'Authorization': 'Bearer ' + token_response['access_token'],
            'Content-Type': 'application/octet-stream'
        }
        file_name = file.filename
        file_content = file.read()
        file.seek(0)

        endpoint = f'https://graph.microsoft.com/v1.0/sites/{app_config.site_id}/drive/items/{app_config.parent_folder2_id}:/{file_name}:/content'

        response = requests.put(endpoint, headers=headers, data=file_content)

        if response.status_code in (200, 201):
            file_info = response.json()
            file_id = file_info['id']
            return file_id, None
        else:
            return None, response.status_code
    except Exception as e:
        print(f"Error in upload_file_to_sharepoint: {e}")
        if 'response' in locals():
            return None, response.status_code
        else:
            return None, 500

def upload_edited_files(file_content,file_name, auth, app_config):
    try:
        token_response = auth.get_token_for_user(app_config.SCOPE)
        if not token_response:
            return None, 401

        headers = {
            'Authorization': 'Bearer ' + token_response['access_token'],
            'Content-Type': 'application/octet-stream'
        }
        endpoint = f'https://graph.microsoft.com/v1.0/sites/{app_config.site_id}/drive/items/{app_config.Edited_Files}:/{file_name}:/content'

        response = requests.put(endpoint, headers=headers, data=file_content)

        if response.status_code in (200, 201):
            file_info = response.json()
            file_id = file_info['id']
            return file_id, response.status_code
        else:
            return None, response.status_code
    except Exception as e:
        print(f"Error in upload_file_to_sharepoint: {e}")
        if 'response' in locals():
            return None, response.status_code
        else:
            return None, 500

def upload_file_to_specific_folder(file, folder_id, auth, app_config):
    try:
        token_response = auth.get_token_for_user(app_config.SCOPE)
        if not token_response:
            return None

        headers = {
            'Authorization': 'Bearer ' + token_response['access_token'],
            'Content-Type': 'application/octet-stream'
        }
        file_name = file.filename
        file_content = file.read()
        file.seek(0)

        endpoint = f'https://graph.microsoft.com/v1.0/sites/{app_config.site_id}/drive/items/{folder_id}:/{file_name}:/content'
        
        response = requests.put(endpoint, headers=headers, data=file_content)
        
        if response.status_code in (200, 201):
            file_info = response.json()
            file_id = file_info['id']
            return file_id
        else:
            return None
    except Exception as e:
        print(f"Error in upload_file_to_specific_folder: {e}")
        return None

def list_files(auth, folder_id=None, app_config=None):
    token_response = auth.get_token_for_user(app_config.SCOPE)
    if not token_response:
        return None, None, None, None, 401

    headers = {
        'Authorization': 'Bearer ' + token_response['access_token'],
        'Accept': 'application/json'
    }

    if folder_id:
        endpoint = f'https://graph.microsoft.com/v1.0/sites/{app_config.site_id}/drive/items/{folder_id}/children'
    else:
        endpoint = f'https://graph.microsoft.com/v1.0/sites/{app_config.site_id}/drive/items/{app_config.parent_folder2_id}/children'
    
    response = requests.get(endpoint, headers=headers)
    
    if response.status_code == 200:
        items = response.json()['value']
        files = [item for item in items if 'file' in item]
        file_ids = [item['id'] for item in files]

        folders = [item for item in items if 'folder' in item]
        folder_ids = [item['id'] for item in folders]
        return files, folders, file_ids, folder_ids, response.status_code
    else:
        return None, None, None, None, response.status_code

def download_file(file_id, auth, app_config):
    token_response = auth.get_token_for_user(app_config.SCOPE)
    if not token_response:
        return None, 401

    headers = {
        'Authorization': 'Bearer ' + token_response['access_token'],
        'Accept': 'application/octet-stream'
    }

    endpoint = f'https://graph.microsoft.com/v1.0/sites/{app_config.site_id}/drive/items/{file_id}/content'
    
    response = requests.get(endpoint, headers=headers, stream=True)
    
    if response.status_code == 200:
        return BytesIO(response.content),  response.status_code
    else:
        return None, response.status_code

def create_folder(folder_name, auth, app_config):
    token_response = auth.get_token_for_user(app_config.SCOPE)
    if not token_response:
        return None, 401

    headers = {
        'Authorization': 'Bearer ' + token_response['access_token'],
        'Content-Type': 'application/json'
    }

    endpoint = f'https://graph.microsoft.com/v1.0/sites/{app_config.site_id}/drive/items/{app_config.parent_folder2_id}/children'
    
    if folder_name:
        # フォルダが存在するか確認
        response = requests.get(endpoint, headers=headers)
        if response.status_code in (200, 201):
            children = response.json().get('value', [])
            for child in children:
                if child.get('name') == folder_name and 'folder' in child:
                    return child['id'], None
        else:
            return None, response.status_code

    # フォルダ名がない場合、新規作成
    folder_data = {
        "name": folder_name,
        "folder": {},
        "@microsoft.graph.conflictBehavior": "rename"
    }

    response = requests.post(endpoint, headers=headers, json=folder_data)
    
    if response.status_code in (200, 201):
        folder_id = response.json().get('id')
        return folder_id, response.status_code
    else:
        return None, response.status_code

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

# ファイル名からIDを抽出する関数
def id_from_filename(filename):
    # 正規表現を使って、ID_数字_ の形式にマッチングする部分を探す
    match = re.search(r'ID_(\d+)_', filename)

    if match:
        # マッチングした部分を整数に変換して返す
        id_num = int(match.group(1))
        return id_num
    else:
        # マッチングしなかった場合はエラーを発生させる
        raise ValueError(f"Invalid filename format: {filename}")