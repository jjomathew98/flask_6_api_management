# flask_6_api_management
## Flask-based RESTful API
Initially, I created flask examples named app_basic.p and app_flasgger.py using the templates provided. Then created an app.py flask template for this assignment, to get a json file as an output ran this application by typing in python app.py in the shell terminal{ "message": "Hello JOHN SMITH!" }

## Azure API deployment and Flassger
Follow this guide and this guide

1. In order to install Azure CLI, type in curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
2. Type in az login --use-device-code and follow instructructins by clicking the link provided and typing in the password provided/
3. Type in sudo apt-get install azure-functions-core-tools-4 to install Azure Functions Core Tools for Linux
4. Type func init LocalFunctionProj --python -m V2 to create Azure Functions project folder
5. Open local.settings.json folder and verify that AzureWebJobsFeatureFlags is equal to EnableWorkerIndexing
6. Go to Azure and search storage. Create a new storage. Access the storage and go to Acess keys. Copy the connection string under any of the keys.
7. Go back to the folder in the shell enviorment and find AzureWebJobsStorage. Paste the connection string after.
8. In your function_app.py under the LocalFunctionProj replace contents with the chosen code and reformat it following the guide. For example, for mine I inserted this code
9. In the terminal, cd into the LocalFunctionProj then type func start.
10. Type az functionapp create --resource-group <resource group name> --consumption-plan-location eastus --runtime python --runtime-version 3.9 --functions-version 4 --name <app name> --os-type linux --storage-account <storage account name>. Replace with your resource group name, a chosen app name, and the storage account name created in Azure. This will create the API connection.
11. Type: func azure functionapp publish <app name> and replace the app name with the chosen app name from the prior step.
12. Images of the API and flassger can be seen in the screenshots folder
