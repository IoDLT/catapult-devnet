# todo: replace resources.json with proper params
import json
import sys

api_key = sys.argv[1]
# client_pk = sys.argv[2]

with open('resources/rest.json', 'r') as f:
    data = json.load(f)
     # other rest options here
    data["db"]["url"] = "mongodb://db:27017/"
    # data["clientPrivateKey"] = client_pk
    data["apiNode"]["publicKey"] = api_key
    data["apiNode"]["host"] = "172.28.0.1"
    with open('resources/rest.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
