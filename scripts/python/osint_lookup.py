#This is script will query VirusTotal for threat intelligence with a given IP address.

import requests
import os

API_KEY = os.environ.get("VT_API_KEY")
if not API_KEY:
    print("Error: VT_API_KEY not set. Run: export VT_API_KEY='your-key-here'")
    exit(1)

IP_ADDRESS = input("Enter IP Address to query: ").strip()

url = f"https://www.virustotal.com/api/v3/ip_addresses/{IP_ADDRESS}"
headers = {"x-apikey": API_KEY}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")

