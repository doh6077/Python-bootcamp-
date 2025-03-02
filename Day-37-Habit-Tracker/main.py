import requests 
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

pixela_endpoint = " https://pixe.la/v1/users"

user_params = {
    "token": TOKEN
}
requests.post()