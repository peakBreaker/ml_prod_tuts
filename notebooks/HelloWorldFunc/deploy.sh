#!/usr/bin/env bash
STORAGE_NAME=mlbasicsazfuncstorage
APP_NAME=javafagpraksismlfunc1

az group create --name AzureFunctionsQuickstart-rg --location westeurope

az storage account create --name $STORAGE_NAME --location westeurope --resource-group AzureFunctionsQuickstart-rg --sku Standard_LRS

az functionapp create --resource-group AzureFunctionsQuickstart-rg --os-type Linux --consumption-plan-location westeurope --runtime python --runtime-version 3.7 --functions-version 2 --name $APP_NAME --storage-account $STORAGE_NAME

func azure functionapp publish $APP_NAME
