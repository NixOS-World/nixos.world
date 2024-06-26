# create_dns_records.py
import json
import requests
import os

with open('records.json') as f:
    records = json.load(f)

api_key = os.getenv('API_KEY')
secret_api_key = os.getenv('SECRET_API_KEY')

ttl = "600"
record_type = "CNAME"

for record in records:
    name = record['name']
    content = record['domain']

    data = {
        "secretapikey": secret_api_key,
        "apikey": api_key,
        "name": name,
        "type": record_type,
        "content": content,
        "ttl": ttl
    }

    response = requests.post("https://api.porkbun.com/api/json/v3/dns/create/nixos.world", json=data)

    if response.status_code == 200:
        print(f"Successfully created DNS record for {name}.nixos.world")
    else:
        print(f"Failed to create DNS record for {name}.nixos.world: {response.text}")
