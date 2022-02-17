import requests
from requests.auth import HTTPBasicAuth
import json

'''
change the url variable ending to retrieve different data
Issue_Sec_Scheme = "api/2/issue/issuesecurityschemes"
Permission_Scheme = "permissionscheme"
Notif_Scheme = "notificationscheme"
P_Category = "api/2/project/projectCategory"
Wflow_Scheme = "workflowscheme"
Issue Create Metadata = "api/2/issue/createmeta"
Project info = "api/2/project/search"
for more info look for GETs in https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-projects/#api-rest-api-2-project-post
'''

#Insert TOKEN below, for more info go to https://id.atlassian.com/manage-profile/security/api-tokens
url = "https://iqualldev.atlassian.net/rest/api/2/issue/createmeta"

auth = HTTPBasicAuth("francisco.chalen@iquall.net", "TOKEN")

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
