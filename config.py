# !/bin/python3

import json
import sys
import fileinput

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
                      "file": "core-node/config/resources/config-node.properties"},
                     {"name": "host =", "param": "127.0.0.1", "file": "core-node/config/resources/config-node.properties"}]

for param in params_to_replace:
    new_param = "{} {}".format(
        param["name"], param["param"])
    print(param["file"])
    for line in fileinput.input(param["file"], inplace=True):
        print(line.rstrip().replace(param["name"], new_param))
print("done")

with open('rest/rest.json', 'r') as f:
    data = json.load(f)
    # other rest options here
    data["db"]["url"] = "mongodb://db:27017/"
    data["clientPrivateKey"] = client_pk
    data["apiNode"]["publicKey"] = api_key
    data["apiNode"]["host"] = "172.28.0.1"
    with open('rest/rest.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
