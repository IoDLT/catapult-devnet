# !/bin/python3

import json
import sys
import re

harvester_key = ""
harvester_vrf = ""
node_name = ""

with open('./config.json', 'r') as f:
    data = json.load(f)

    harvester_key = data["harvesterKey"]
    harvester_vrf = data["harvesterVrfKey"]
    node_name = data["nodeName"]

params_to_replace = [
    {"name": "harvesterSigningPrivateKey =", "param": harvester_key,
     "file": "core-node/config/resources/config-harvesting.properties"},
    {"name": "harvesterVrfPrivateKey =", "param": harvester_vrf,
     "file": "core-node/config/resources/config-harvesting.properties"},
    {"name": "friendlyName =", "param": node_name,
     "file": "core-node/config/resources/config-node.properties"}]

for param in params_to_replace:
    new_param = "{} {}".format(
        param["name"], param["param"])
    f = open(param["file"], 'r')
    filedata = f.read()
    f.close()
    newdata = re.sub(
        r'(?<={})[^\n\s]*'.format(param["name"]), param["param"], filedata)
    print(newdata)
    f = open(param["file"], 'w')
    f.write(newdata)
    f.close()

with open('rest/rest.json', 'r') as f:
    data = json.load(f)
    # other rest options here
    data["db"]["url"] = "mongodb://db:27017/"
    data["apiNode"]["host"] = "172.28.1.1"
    with open('rest/rest.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
