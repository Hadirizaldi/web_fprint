import requests
from requests.auth import HTTPDigestAuth,HTTPBasicAuth
from utils import generate_password_md5, generate_username

API_URL = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

data = {
  'username': generate_username(),
  'password' : generate_password_md5()
}

# response = requests.post(API_URL, auth=(generate_username(), generate_password_md5()))
response = requests.post(API_URL, data=data)

# print(response.headers)
if response.status_code == 200:
  api_data= response.json()['data']
  for data_product in api_data:
    print (data_product['status'])