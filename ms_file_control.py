import requests
from flask import flash, redirect, url_for
from io import BytesIO

def upload_file_to_sharepoint(file, auth, app_config):
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

        endpoint = f'https://graph.microsoft.com/v1.0/sites/{app_config.site_id}/drive/items/{app_config.parent_folder2_id}:/{file_name}:/content'
        
        response = requests.put(endpoint, headers=headers, data=file_content)
        
        if response.status_code in (200, 201):
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error in upload_file_to_sharepoint: {e}")
        return None

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
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error in upload_file_to_specific_folder: {e}")
        return None

def list_files(auth, app_config, folder_id=None):
    token_response = auth.get_token_for_user(app_config.SCOPE)
    if not token_response:
        return None, "トークンが取得できませんでした。", 401

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
        items = response.json().get('value', [])
        files = [item for item in items if 'file' in item]
        folders = [item for item in items if 'folder' in item]
        return files, folders, None, None
    else:
        return None, None, "ファイルリストの取得に失敗しました。", response.status_code

def download_file(file_id, auth, app_config):
    token_response = auth.get_token_for_user(app_config.SCOPE)
    if not token_response:
        return None, "トークンが取得できませんでした。", 401

    headers = {
        'Authorization': 'Bearer ' + token_response['access_token'],
        'Accept': 'application/json'
    }

    endpoint = f'https://graph.microsoft.com/v1.0/sites/{app_config.site_id}/drive/items/{file_id}/content'
    
    response = requests.get(endpoint, headers=headers, stream=True)
    
    if response.status_code == 200:
        return BytesIO(response.content), None, 200
    else:
        return None, "ファイルのダウンロードに失敗しました。", response.status_code

def create_folder(folder_name, auth, app_config):
    token_response = auth.get_token_for_user(app_config.SCOPE)
    if not token_response:
        return None, "トークンが取得できませんでした。", 401

    headers = {
        'Authorization': 'Bearer ' + token_response['access_token'],
        'Content-Type': 'application/json'
    }

    endpoint = f'https://graph.microsoft.com/v1.0/sites/{app_config.site_id}/drive/items/{app_config.parent_folder2_id}/children'
    
    if folder_name:
        # フォルダが存在するか確認
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            children = response.json().get('value', [])
            for child in children:
                if child.get('name') == folder_name and 'folder' in child:
                    return child['id'], None
        else:
            return None, "フォルダの確認に失敗しました。"

    # フォルダ名がない場合、新規作成
    folder_data = {
        "name": folder_name,
        "folder": {},
        "@microsoft.graph.conflictBehavior": "rename"
    }

    response = requests.post(endpoint, headers=headers, json=folder_data)
    
    if response.status_code == 201:
        folder_id = response.json().get('id')
        return folder_id, None
    else:
        return None, "フォルダの作成に失敗しました。"
