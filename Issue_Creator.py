import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd

url = "https://iqualldev.atlassian.net/rest/api/2/issue"

#Insert USER and TOKEN below, for more info go to https://id.atlassian.com/manage-profile/security/api-tokens
auth = HTTPBasicAuth("USER", "TOKEN")

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

epic_number_result = ""

issue_number_result = ""

issue_list = []

#Function to create an Epic
def create_epic(summary, project_ID, issue_type, description = "No Description"):
  payload = json.dumps({
    "fields": {
      "summary": summary,
      "issuetype": {
        "id": issue_type
      },
      "project": {
        "id": project_ID
      },
      "description": description,
      "customfield_10011": summary
    }
  })

  response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
  )

  x1 = json.loads(response.text)

  issue_list.append(x1)

  return x1

#Function to create a generic issue
def create_issue(summary, project_ID, issue_type, parent_id, description = "No Description"):
  payload = json.dumps({
    "fields": {
      "summary": summary,
      "issuetype": {
        "id": str(issue_type)
      },
      "project": {
        "id": str(project_ID)
      },
      "parent": {
      "id": str(parent_id)
      },
      "description": description
    }
  })

  response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
  )

  x1 = json.loads(response.text)

  issue_list.append(x1)

  return x1

'''
issue types:
Epic: 10000
Task: 10007
Sub-task: 10008
Bug: 10009
Story: 10013
'''

def create_from_template(df, project_id):
  epics = []
  stories = []
  epic_numbers = []
  #Proj_df = pd.read_csv(file)
  df_epics = df[df['Type'] == 'Epic']
  df_stories = df[df['Type'] == 'Story']
  for index, row in df_epics.iterrows():
    epic = create_epic(row['Name'], project_id, 10000, 'Issue description')
    #epic = row['Name']
    epic_id = epic['id']
    epics.append(epic)
    df_epics.loc[index, 'Epic_number'] = epic_id

  for index, row in df_stories.iterrows():
    epic_loc = (row['Epic'] == df_epics['Name'])
    row['Epic_number'] = df_epics.loc[epic_loc, 'Epic_number'].iat[0]
    print(row)
    story = create_issue(row['Name'], project_id, 10013, row['Epic_number'], 'Issue description')
    story_id = story['id']
    stories.append(story)
    df_stories.loc[index, 'Epic_number'] = row['Epic_number']
    #df_stories.at[index, 'Epic_number'] = epic_number
    #df_stories.set_value(index, 'St_')

  return df_epics, df_stories


#print (create_from_template('data.csv'))

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

print(create_issue("prueba", 10104, 10009, 18853, description = "No Description"))

