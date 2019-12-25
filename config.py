# !/bin/python3

import json
import sys
import re

harvester_key = ""
boot_key = ""
node_name = ""
api_key = ""
client_pk = ""

with open('./config.json', 'r') as f:
    data = json.load(f)

    harvester_key = data["harvesterKey"]
    boot_key = data["bootKey"]
    node_name = data["nodeName"]
    api_key = data["apiKey"]
    client_pk = data["clientPk"]

params_to_replace = [{"name": "bootPrivateKey =", "param": boot_key, "file": "core-node/config/resources/config-user.properties"},
                     {"name": "harvesterPrivateKey =", "param": harvester_key,
                      "file": "core-node/config/resources/config-harvesting.properties"},
                     {"name": "friendlyName =", "param": node_name,
                      "file": "core-node/config/resources/config-node.properties"}]

for param in params_to_replace:
    new_param = "{} {}".format(
        param["name"], param["param"])
    f = open(param["file"],'r')
    filedata = f.read()
    f.close()
    newdata = re.sub(r'(?<={})[^\n\s]*'.format(param["name"]), param["param"], filedata)
    print(newdata)
    f = open(param["file"],'w')
    f.write(newdata)
    f.close()

with open('rest/rest.json', 'r') as f:
    data = json.load(f)
    # other rest options here
    data["db"]["url"] = "mongodb://db:27017/"
    data["clientPrivateKey"] = client_pk
    data["apiNode"]["publicKey"] = api_key
    data["apiNode"]["host"] = "172.28.1.1"
    with open('rest/rest.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
