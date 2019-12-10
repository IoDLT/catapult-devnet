# !/bin/python3

import sys
import fileinput

harvester_key = sys.argv[1]
boot_key = sys.argv[2]
node_name = sys.argv[3]

params_to_replace = [{"name": "bootPrivateKey =", "param": boot_key},
                     {"name": "harvesterPrivateKey =", "param": harvester_key},
                     {"name": "friendlyName =", "param": node_name}]

files_to_replace = ["/usr/src/app/node/resources/config-user.properties",
                    "/usr/src/app/node/resources/config-harvesting.properties", "/usr/src/app/node/resources/config-node.properties"]


print(params_to_replace)

for idx, file in enumerate(files_to_replace):
    new_param = "{} {}".format(
        params_to_replace[idx]["name"], params_to_replace[idx]["param"])
    search = "{}".format(params_to_replace[idx]["name"])
    print(file)
    for line in fileinput.input(file, inplace=True):
        print(line.rstrip().replace(params_to_replace[idx]["name"], new_param))
print("done")
