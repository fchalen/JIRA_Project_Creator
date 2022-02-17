import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://iqualldev.atlassian.net/rest/api/2/project"

#Insert TOKEN below, for more info go to https://id.atlassian.com/manage-profile/security/api-tokens
auth = HTTPBasicAuth("francisco.chalen@iquall.net", "TOKEN")

headers = {
"Accept": "application/json",
"Content-Type": "application/json"
}

#project_Key = "TST009"

#project_Name = "Proyecto Test 009"

def createProject(project_Key, project_Name, project_Description, project_Category):
   payload = json.dumps( {
   "key": project_Key,
   "name": project_Name,
   "projectTypeKey": "software",
   "projectTemplateKey": "com.pyxis.greenhopper.jira:gh-simplified-scrum-classic",
   "description": project_Description,
   "leadAccountId": "609ede6c391e56006e2074c0",
   "url": "http://atlassian.com",
   "assigneeType": "PROJECT_LEAD",
   "avatarId": 10200,
   "issueSecurityScheme": 10006,
   "permissionScheme": 10011,
   "notificationScheme": 10000,
   "categoryId": project_Category } )

   response = requests.request(
      "POST",
      url,
      data=payload,
      headers=headers,
      auth=auth
   )

   x1 = json.loads(response.text)

   return x1

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


""" Valid project templates are: com.pyxis.greenhopper.jira:gh-simplified-agility-kanban, 
com.pyxis.greenhopper.jira:gh-simplified-agility-scrum, com.pyxis.greenhopper.jira:gh-simplified-basic, 
com.pyxis.greenhopper.jira:gh-simplified-kanban-classic, com.pyxis.greenhopper.jira:gh-simplified-scrum-classic, 
com.atlassian.servicedesk:simplified-it-service-management, com.atlassian.servicedesk:simplified-general-service-desk, 
com.atlassian.servicedesk:simplified-internal-service-desk, com.atlassian.servicedesk:simplified-external-service-desk, 
com.atlassian.servicedesk:simplified-hr-service-desk, com.atlassian.servicedesk:simplified-facilities-service-desk, 
com.atlassian.servicedesk:simplified-legal-service-desk, 
com.atlassian.jira-core-project-templates:jira-core-simplified-content-management, 
com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval, 
com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking, 
com.atlassian.jira-core-project-templates:jira-core-simplified-process-control, 
com.atlassian.jira-core-project-templates:jira-core-simplified-procurement, 
com.atlassian.jira-core-project-templates:jira-core-simplified-project-management, 
com.atlassian.jira-core-project-templates:jira-core-simplified-recruitment, 
com.atlassian.jira-core-project-templates:jira-core-simplified-task-"""
