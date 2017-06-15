import requests
import xmltodict
import json
import os


credentials = {"username": "user", "password": "pass"}

# Read file name, Looking for Matching Identifier, Change File name to Match PID, Save


def update_filenames(x, url):
    for item in os.walk(x):
        for record in item[2]:
            r = requests.get("{0}?query=identifier%7E{1}&pid=true&resultFormat=xml".format(url, record.strip('.xml')),
                             auth=(credentials['username'], credentials['password']))
            json_string = json.dumps(xmltodict.parse(r.text))
            json_document = json.loads(json_string)
            print(json_document["result"])

if __name__ == "__main__":
    path = '../modsxml/'
    base_url = 'http://localhost:8080/fedora/objects/'
    update_filenames(path, base_url)