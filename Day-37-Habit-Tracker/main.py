import requests 
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
USERNAME = "doheek"
pixela_endpoint = " https://pixe.la/v1/users"



user_params = {
    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService":"yes", "notMinor":"yes"
}
response = requests.post(url = pixela_endpoint, json= user_params)

print(response.text)