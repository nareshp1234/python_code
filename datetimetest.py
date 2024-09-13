'''
from datetime import datetime
import datetime as dt
import sys

def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%dT%H:%M:%SZ'):
            raise ValueError
        else:
            print("valid time")

        return True
    except ValueError:
        return False
    
def main():
    # validate("2024-08-22T16:31:11Z")
    #validate("2024-08-22 16:44:34.578948")


import datetime as dt
# from datetime import datetime, timedelta
tod = dt.datetime.now()
print(tod.strftime("%Y-%m-%dT%H:%M:%SZ"))
d = dt.timedelta(days = 5)
a = tod - d
print(a.strftime("%y-%m-%d"))
'''

import requests
import subprocess
import json
import csv
from requests.auth import HTTPBasicAuth

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

SOURCE_JPD_URL=""
JPD_USERNAME=""
JPD_TOKEN=""
'''
data = {
            "url" : "https://<artifactoryurl>/artifactory/blr-docker-dev-local",
            "socketTimeoutMillis" : 15000,
            "username" : "nareshp",
            "password" : "Rakul123@#",
            "enableEventReplication" : "false",
            "enabled" : "true",
            "cronExp" : "0 0 12 * * ?",
            "syncDeletes" : "true",
            "syncProperties" : "true",
            "syncStatistics" : "false",
            "repoKey" : "blr-docker-dev-local",
            "includePathPrefixPattern" : "/path/to/repo",    
            "excludePathPrefixPattern" : "/path/to/repo", 
            "checkBinaryExistenceInFilestore" : "false" 
            }
response = requests.post(SOURCE_JPD_URL+ "/artifactory/api/replications/blr-docker-dev-local", json=data,  auth=HTTPBasicAuth(JPD_USERNAME, JPD_TOKEN))
if(response.status_code== 200):
    print("Replication configuration update is success")
else:
    print ("Unable to configure replication for repo ==> blr-docker-dev-local")
    print(response.text)
'''
headers = {
            "Authorization": "Bearer "+JPD_TOKEN,
            "Accept": "text/plain",
            "Content-Type": "text/plain"
            }
''''
response = requests.get(SOURCE_JPD_URL+ "/artifactory/api/repositories?type=local", headers=headers)
if(response.status_code== 200):
    print("Replication configuration update is success")
    data=response.json()
    rep_str = json.dumps(data, indent=4)
    print(rep_str)
else:
    print ("Unable to configure replication for repo ==> blr-docker-dev-local")
    print(response.text)
'''
# artifacts_in_repo = 'items.find({"repo":"blrcuration-docker-dev-virtual"}).include("repo","path","name","created")'
artifacts_in_repo = 'items.find({"repo":"blrcuration-docker-dev-virtual"}).include("repo","path","name","created")'
response = requests.post(SOURCE_JPD_URL+ "/artifactory/api/search/aql" , data=artifacts_in_repo, headers=headers)
if(response.status_code== 200):
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    data=response.json()
    rep_str = json.dumps(data, indent=4)
    print(rep_str)
else:
    print ("Unable to configure replication for repo ==> blr-docker-dev-local")
    print(response.text)

CHUNK_SIZE = 5
pattern=[]
artifactslistjson = json.loads(rep_str)
#print(artifactslistjson["range"]["total"])

if artifactslistjson["range"]["total"] > CHUNK_SIZE:
    print("getting chunk")
    #print(artifactslistjson["results"])
    result=artifactslistjson["results"][:CHUNK_SIZE]

    for item in data["results"]:
        if item["path"] not in pattern:
            pattern.append(item["path"])
        
    print(pattern)
    #mylist = artifactslistjson["results"][0][CHUNK_SIZE]
    #print( str(mylist))
    #for path in enumerate(mylist):
    #   print(path)
        #results.append(path)
    #print(results)


'''
response = requests.get(SOURCE_JPD_URL+ "/xray/api/v1/artifacts?&repo=blrcuration-docker-dev-virtual", headers=headers)
if(response.status_code== 200):
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    data=response.json()
    rep_str = json.dumps(data, indent=4)
    print(rep_str)
else:
    print ("Unable to configure replication for repo ==> blr-docker-dev-local")
    print(response.text)



if __name__ == "__main__":
    main()
'''
