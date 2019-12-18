## !!! STILL IN PROGRESS, NOT STABLE !!! 

# Catapult Community Testnet
This repo will contain the settings, nemesis block information, and deployment needed for the Catapult community testnet. As more information is decided (explanations behind the settings of this network), this repo will be added to as the testnet progresses.

The node configured launches a dual node, meaning it has both Peer and Api roles.  

# Prerequisites 

* [Docker](https://docs.docker.com/v17.09/engine/installation/)

* [Docker compose](https://docs.docker.com/compose/install/)

* Node keypair

* Harvester private key

* Python

# Running

To run your node, fill out the `config.json` found in the base of this repo:

```json
{
    "harvesterKey": "<your-harvester-key>",
    "bootKey": "<your-node-key>",
    "apiKey": "<your-node-public-key>",
    "nodeName": "<your-name>",
    "clientPk": "<private-key-for-REST>"
}
```

Note: ensure the `clientPk` is NOT the boot key.

Once this is done, run:
```sh
python config.py
```

And, finally:
```sh
bash start.sh
```


# Catapult Dependencies

The directory `catapult-deps/` contains a Docker configuration for installing and compiling Catapult and its dependencies into one image.  Currently, this image is [pre-built](https://hub.docker.com/repository/docker/crackthecode01/catapult-deps) and used to run Catapult as per the Dockerfile in `core-node/`.  To build this image yourself is simple: 

```
cd catapult-deps/
docker build -t catapult-deps .
```

Then, make sure to use this as your builder in `core-node/Dockerfile`

```diff
- FROM crackthecode01/catapult-deps:latest as builder
+ FROM catapult-deps as builder
```
