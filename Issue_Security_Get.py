import requests
from requests.auth import HTTPBasicAuth
import json

#Issue_Sec_Scheme = "issuesecurityschemes"
#Permission_Scheme = "permissionscheme"
#Notif_Scheme = "notificationscheme"
#P_Category = "projectCategory"
#Wflow_Scheme = "workflowscheme"


url = "https://iqualldev.atlassian.net/rest/api/2/issue/createmeta"

auth = HTTPBasicAuth("francisco.chalen@iquall.net", "39GnxVeP4l3kuWRBDq8463C3")

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