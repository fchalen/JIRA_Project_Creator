import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://iqualldev.atlassian.net/rest/api/2/project"

#Insert USER and TOKEN below, for more info go to https://id.atlassian.com/manage-profile/security/api-tokens
auth = HTTPBasicAuth("USER", "TOKEN")

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
