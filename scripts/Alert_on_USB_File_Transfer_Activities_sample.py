
# Alert on USB File Transfer Activities (via Defender for Endpoint)

# This script checks Microsoft Defender for Endpoint’s advanced hunting API for USB activity by potential insider risk users.

import requests, msal

query = """
DeviceEvents
| where ActionType == "UsbDriveMounted"
| where Timestamp > ago(1d)
"""

def run_advanced_hunting(query, token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(
        url="https://api.securitycenter.microsoft.com/api/advancedqueries/run",
        headers=headers,
        json={"Query": query}
    )
    return response.json()["Results"]

# Assume Defender ATP app registration and token retrieval is done
results = run_advanced_hunting(query, token['access_token'])

for item in results:
    print(f"🔌 USB mounted: {item['DeviceName']} by {item['InitiatingProcessAccountName']} at {item['Timestamp']}")
