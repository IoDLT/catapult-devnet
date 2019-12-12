# !/bin/python3

# configures .properties files for the Catapult node

import sys
import fileinput

harvester_key = sys.argv[1]
boot_key = sys.argv[2]
node_name = sys.argv[3]

params_to_replace = [{"name": "bootPrivateKey =", "param": boot_key, "file": "./resources/config-user.properties"},
                     {"name": "harvesterPrivateKey =", "param": harvester_key,
                         "file": "./resources/config-harvesting.properties"},
                     {"name": "friendlyName =", "param": node_name,
                         "file": "./resources/config-node.properties"},
                     {"name": "host =", "param": "127.0.0.1", "file": "./resources/config-node.properties"}]

for param in params_to_replace:
    new_param = "{} {}".format(
        param["name"], param["param"])
    print(param["file"])
    for line in fileinput.input(param["file"], inplace=True):
        print(line.rstrip().replace(param["name"], new_param))
print("done")
