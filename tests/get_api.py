import requests
from django.http import request
base_url ="http://localhost:8000/api/v1/"
api_url ="worker_list/"
full_url=base_url+api_url
print(full_url)
resp_data = requests.get(full_url).json()
print("get resp data",resp_data)



