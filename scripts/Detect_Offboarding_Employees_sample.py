
# Detect Offboarding Employees with HR Attribute Filters (Graph API)

# This script pulls Azure AD users with a terminationDate set — a signal used to populate "Departing Employee" 
# risk policies in Microsoft Purview IRM.

import requests
import msal

TENANT_ID = "your-tenant-id"
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

app = msal.ConfidentialClientApplication(
    CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET
)
token = app.acquire_token_for_client(scopes=SCOPE)
headers = {"Authorization": f"Bearer {token['access_token']}"}

# Get users with a terminationDateTime set
endpoint = "https://graph.microsoft.com/v1.0/users?$filter=onPremisesExtensionAttributes/extensionAttribute1 ne null"
response = requests.get(endpoint, headers=headers)
users = response.json()["value"]

for user in users:
    print(f"{user['displayName']} - {user.get('onPremisesExtensionAttributes', {}).get('extensionAttribute1')}")



