#This is script will query VirusTotal for threat intelligence with a given IP address.

import requests

API_KEY = "your-virustotal-api-key"
IP_ADDRESS = "8.8.8.8"  # Replace with a target IP

url = f"https://www.virustotal.com/api/v3/ip_addresses/{IP_ADDRESS}"
headers = {"x-apikey": API_KEY}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")

