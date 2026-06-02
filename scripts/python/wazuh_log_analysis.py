#!/usr/bin/env python3
"""
This script queries Wazuh API for security alerts and log analysis.
"""

import requests
import os
import sys
import json
from datetime import datetime, timedelta

# Wazuh API configuration
WAZUH_API_URL = os.environ.get("WAZUH_API_URL", "http://localhost:55000")
WAZUH_USERNAME = os.environ.get("WAZUH_USERNAME", "wazuh")
WAZUH_PASSWORD = os.environ.get("WAZUH_PASSWORD")

if not WAZUH_PASSWORD:
    print("Error: WAZUH_PASSWORD not provided")
    exit(1)

# Disable SSL warnings for self-signed certificates
requests.packages.urllib3.disable_warnings()

def get_auth_token():
    """Authenticate with Wazuh API"""
    auth_url = f"{WAZUH_API_URL}/security/user/authenticate"
    try:
        response = requests.post(auth_url, auth=(WAZUH_USERNAME, WAZUH_PASSWORD), verify=False)
        if response.status_code == 200:
            return response.json()['data']['token']
        else:
            print(f"Authentication failed: {response.status_code}")
            exit(1)
    except Exception as e:
        print(f"Error connecting to Wazuh API: {e}")
        exit(1)

def get_alerts(token, hours=24):
    """Fetch security alerts from Wazuh"""
    headers = {"Authorization": f"Bearer {token}"}
    
    # Get alerts from the last 24 hours
    alerts_url = f"{WAZUH_API_URL}/alerts"
    params = {
        "query": "select * from alerts",
        "limit": 100
    }
    
    try:
        response = requests.get(alerts_url, headers=headers, params=params, verify=False)
        if response.status_code == 200:
            alerts = response.json()
            print(f"Retrieved {len(alerts.get('data', {}).get('affected_items', []))} alerts from Wazuh")
            return alerts
        else:
            print(f"Failed to fetch alerts: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching alerts: {e}")
        return None

def analyze_alerts(alerts):
    """Analyze and summarize alerts"""
    if not alerts:
        print("No alerts to analyze")
        return
    
    items = alerts.get('data', {}).get('affected_items', [])
    
    if not items:
        print("No alert items found")
        return
    
    # Group alerts by severity
    severity_count = {}
    agent_count = {}
    
    for alert in items:
        severity = alert.get('rule', {}).get('level', 'unknown')
        agent_id = alert.get('agent', {}).get('id', 'unknown')
        
        severity_count[severity] = severity_count.get(severity, 0) + 1
        agent_count[agent_id] = agent_count.get(agent_id, 0) + 1
    
    print("\n=== Alert Summary ===")
    print(f"Total Alerts: {len(items)}")
    print("\nAlerts by Severity:")
    for severity, count in sorted(severity_count.items(), reverse=True):
        print(f"  Level {severity}: {count} alerts")
    
    print("\nAlerts by Agent:")
    for agent_id, count in sorted(agent_count.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  Agent {agent_id}: {count} alerts")

if __name__ == "__main__":
    print(f"Connecting to Wazuh API at {WAZUH_API_URL}")
    
    # Authenticate
    token = get_auth_token()
    print("Successfully authenticated with Wazuh")
    
    # Fetch and analyze alerts
    alerts = get_alerts(token)
    if alerts:
        analyze_alerts(alerts)
        print("\nWazuh log analysis completed successfully")
    else:
        print("Failed to retrieve alerts from Wazuh")
        exit(1)

