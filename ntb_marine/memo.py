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


