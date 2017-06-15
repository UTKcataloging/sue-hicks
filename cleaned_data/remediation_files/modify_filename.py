import requests
import xmltodict
import json
import os


credentials = {"username": "user", "password": "pass"}

# Read file name, Looking for Matching Identifier, Change File name to Match PID, Save


def update_filenames(x, url):
    for item in os.walk(x):
        for record in item[2]:
            print(record.strip('.xml'))
            r = requests.get("{0}?query=identifier%7E{1}&pid=true".format(url, record.strip('.xml')), auth=(credentials['username'], credentials['password']))
            print(r)

if __name__ == "__main__":
    path = '../modsxml/'
    base_url = 'http://localhost:8080/fedora/objects/'
    update_filenames(path, base_url)