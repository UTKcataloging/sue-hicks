import requests
import xmltodict
import json
import os
import shutil


credentials = {"username": "user", "password": "pass"}

# Read file name, Looking for Matching Identifier, Change File name to Match PID, Save


def update_filenames(x, url):
    for item in os.walk(x):
        for record in item[2]:
            print("Looking for {0}".format(record))
            r = requests.get("{0}?query=identifier%7E*{1}*&pid=true&resultFormat=xml".format(url, record.strip('.xml')),
                             auth=(credentials['username'], credentials['password']))
            json_string = json.dumps(xmltodict.parse(r.text))
            json_document = json.loads(json_string)
            pid = json_document["result"]["resultList"]["objectFields"]["pid"]
            print("\tMoving {0} to {1}.".format(record,json_document["result"]["resultList"]["objectFields"]["pid"]))
            shutil.copyfile("{0}{1}".format(x,record), "output/{0}.xml".format(pid))

if __name__ == "__main__":
    path = '../modsxml/'
    base_url = 'http://localhost:8080/fedora/objects/'
    update_filenames(path, base_url)