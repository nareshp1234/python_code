import requests
import sys
import json
import subprocess
from requests.auth import HTTPBasicAuth
import datetime as dt
from datetime import datetime, timedelta

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# get number of days
numberofdays = sys.argv[0]
print(numberofdays)


SOURCE_JPD_URL=""
JPD_USERNAME=""
JPD_TOKEN=""

# Get release bundles
response = requests.get(SOURCE_JPD_URL+ "/lifecycle/api/v2/release_bundle/names", auth=HTTPBasicAuth(JPD_USERNAME, JPD_TOKEN))
data=response.json()

# list of release bundles
listofrb = data["release_bundles"]
for i in listofrb:
    rbname = i["release_bundle_name"]
    print("Release bundle name : " + rbname)
    # Get versions for RB
    response = requests.get(SOURCE_JPD_URL+ "/lifecycle/api/v2/release_bundle/records/" + rbname, auth=HTTPBasicAuth(JPD_USERNAME, JPD_TOKEN))
    if (response.status_code==200):
        rbversions=response.json()
        rbversionlist = rbversions["release_bundles"]
        for k in rbversionlist:
            createddate = k["created"]
            date_str = createddate.split("T")[0]
            # convert string to date format
            date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
            print(" Date object " + date_str)

            # Get date after number of days
            tod = dt.datetime.now()
            d = dt.timedelta(days = 1)
            a = tod - d
            pastdate = a.strftime("%Y-%m-%d")
            past_object = datetime.strptime(pastdate, '%Y-%m-%d').date()
            print(a.strftime("%Y-%m-%d"))

            if date_object < past_object: 
                print ("true")
            else:
                print ("false")
            
            
           
           

            


            
            

        
                  
    else:
        print("Error in fetching versions of release bundle.")
    

    

