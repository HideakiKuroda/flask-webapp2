@echo off
setlocal

rem Variables
set RESOURCE_GROUP=ntbResourceGroup
set APP_NAME=ntb-marine
set PLAN_NAME=myLinuxAppServicePlan --sku B1
set LOCATION="japanwest"

rem Azure CLI login (Make sure you
rem az login

rem Create Resource Group
rem echo Creating Resource Group...
rem az group create --name %RESOURCE_GROUP% --location %LOCATION%

rem Create App Service Plan
rem echo Creating App Service Plan...
rem az appservice plan create --name %PLAN_NAME% --resource-group %RESOURCE_GROUP% --sku FREE --is-linux

rem Create Web App
rem echo Creating Web App...
rem az webapp create --resource-group %RESOURCE_GROUP% --plan %PLAN_NAME% --name %APP_NAME% --runtime "PYTHON:3.11"

rem Zip the application
rem echo Zipping the application...
rem powershell Compress-Archive -Path * -DestinationPath app.zip -Force

rem Deploy to Azure
echo Deploying to Azure...
az webapp deploy --resource-group %RESOURCE_GROUP% --name %APP_NAME% --src-path app.zip

rem Set Startup Command (if needed, depends on app structure)
rem az webapp config set --resource-group %RESOURCE_GROUP% --name %APP_NAME% --startup-file "python -m flask run --host=0.0.0.0 --port=8000"

rem Monitor logs
echo Monitoring logs...
az webapp log tail --resource-group %RESOURCE_GROUP% --name %APP_NAME%

endlocal