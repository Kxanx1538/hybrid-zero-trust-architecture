
#  Monitor Suspicious Data Downloads from SharePoint / OneDrive (Audit Log API)

# Detect large file downloads by users tagged as "high-risk" (e.g., in a group like HR_Departures)


from datetime import datetime, timedelta
import requests, msal

GROUP_ID = "your-high-risk-group-id"
LOOKBACK_DAYS = 1

def get_audit_logs(token):
    time_from = (datetime.utcnow() - timedelta(days=LOOKBACK_DAYS)).isoformat() + 'Z'
    url = f"https://graph.microsoft.com/v1.0/auditLogs/signIns?$filter=createdDateTime ge {time_from}"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.get(url, headers=headers).json()["value"]

def is_high_risk(user_id, token):
    url = f"https://graph.microsoft.com/v1.0/groups/{GROUP_ID}/members/{user_id}/$ref"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.get(url, headers=headers).status_code == 204

# Setup MSAL and get token
# [Similar token acquisition as above]
# Then:
logs = get_audit_logs(token['access_token'])

for log in logs:
    if "OneDrive" in str(log.get("resourceDisplayName", "")) and int(log.get("resourceDataSize", 0)) > 1000000:
        if is_high_risk(log["userId"], token['access_token']):
            print(f"⚠️ Suspicious download: {log['userDisplayName']} at {log['createdDateTime']}")
