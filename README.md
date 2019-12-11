## !!! STILL IN PROGRESS, NOT STABLE !!! 

# Catapult Community Testnet
This repo will contain the settings, nemesis block information, and deployment needed for the Catapult community testnet. As more information is decided (explanations behind the settings of this network), this repo will be added to as the testnet progresses.

The node configured launches a dual node, meaning it has both Peer and Api roles.  

# Prerequisites 

* [Docker](https://docs.docker.com/v17.09/engine/installation/)

* [Docker compose](https://docs.docker.com/compose/install/)

* Node keypair

* Harvester private key


# Connecting To The Network

// TODO

# Building + Running Locally

Firstly, open the `Dockerfile` located in `core-node/` of this repo, and replace the following with your own values: 

```Dockerfile
ENV harvester_key=<your-key>
ENV boot_key=<your-key>
ENV node_name=<your-chosen-name>
```

Then, simply run docker-compose in the root of this repo: 

```shell
docker-compose up
```

And your node should be up and running!

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
