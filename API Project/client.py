import requests

API_URL = "http://35.236.248.79:5000/api/time?city=Tokyo"
TOKEN = "supersecrettoken123"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed:", response.status_code, response.text)