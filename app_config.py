import os
AUTHORITY = os.getenv("AUTHORITY")

# Application (client) ID of app registration
CLIENT_ID = os.getenv("CLIENT_ID")
# Application's generated client secret: never check this into source control!
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
site_id = os.getenv('SITE_ID')  # 取得したsite_idを設定
# list_id = os.getenv('LIST_ID')  # 取得したlist_idを設定
# drive_id =  os.getenv('DRIVE_ID')
parent_folder1_id =  os.getenv('PARENT_FOLDER1_ID')  
parent_folder2_id =  os.getenv('PARENT_FOLDER2_ID')  
REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
# The absolute URL must match the redirect URI you set
# in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/sites/ntb3626.sharepoint.com:/sites/ntb-marine'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.Read"]

# Tells the Flask-session extension to store sessions in the filesystem
SESSION_TYPE = "filesystem"
# In production, your setup may use multiple web servers behind a load balancer,
# and the subsequent requests may not be routed to the same web server.
# In that case, you may either use a centralized database-backed session store,
# or configure your load balancer to route subsequent requests to the same web server
# by using sticky sessions also known as affinity cookie.
# [1] https://www.imperva.com/learn/availability/sticky-session-persistence-and-cookies/
# [2] https://azure.github.io/AppService/2016/05/16/Disable-Session-affinity-cookie-(ARR-cookie)-for-Azure-web-apps.html
# [3] https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal#configure-general-settings
