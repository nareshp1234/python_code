

import requests
import json
from requests.auth import HTTPBasicAuth
from urllib.parse import urlparse

SOURCE_JPD_URL=""
JPD_USERNAME="admin"
JPD_TOKEN=""
REPLICATION_URL=""
ENABLE_STATUS=""
REPLICATION_USERNAME=""
REPLICATION_PASSWORD=""

try:
    # Get all local repositories
    response = requests.get(SOURCE_JPD_URL+ "/artifactory/api/repositories?type=local", auth=HTTPBasicAuth(JPD_USERNAME, JPD_TOKEN))
    data=response.json()

    # Get replications for each repo
    for i in data:
        reponame = i["key"]
        url = i["url"]
        response = requests.get(SOURCE_JPD_URL+ "/artifactory/api/replications/" + reponame, auth=HTTPBasicAuth(JPD_USERNAME, JPD_TOKEN))
        replicationdata = response.json()
        
        rep_str = json.dumps(replicationdata, indent=4)
        if (response.status_code==200):
            print("Replication configured for ==> "  + reponame)
            
            # get url field
            currenturl = replicationdata[0]['url']
            
            current_url = urlparse(currenturl)
            # replace url with new value
            current_url= current_url._replace(netloc=REPLICATION_URL).geturl()

            # update the new url and status
            if current_url != "":
                replicationdata[0]['url'] = current_url

            if ENABLE_STATUS != "":
                replicationdata[0]['enabled'] = ENABLE_STATUS

            if REPLICATION_USERNAME != "":
                replicationdata[0]['username'] = REPLICATION_USERNAME

            if REPLICATION_PASSWORD != "":
                replicationdata[0]['password'] = REPLICATION_PASSWORD

            data= replicationdata[0]
            
            #update the replication url and enable status
            response = requests.post(SOURCE_JPD_URL+ "/artifactory/api/replications/" + reponame, json=data,  auth=HTTPBasicAuth(JPD_USERNAME, JPD_TOKEN))
            if(response.status_code== 200):
                print("Replication configuration update is success for repo ==> " + reponame)
            else:
                print ("Unable to configure replication for repo ==> " + reponame)
                print(response._content) 
        else:
            print("No replication configured for repo ==> " + reponame)
  
except BaseException as e:
    print(" Failed to execute script, exception : "+ str(e))
