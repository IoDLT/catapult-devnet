## !!! STILL WORKING ON THIS, NOT STABLE !!! 

# Catapult Community Testnet
This repo will contain the settings, nemesis block information, and deployment needed for the Catapult community testnet. As more information is decided (explanations behind the settings of this network), this repo will be added to as the testnet progresses.

# Prerequisites 

* [Docker](https://docs.docker.com/v17.09/engine/installation/)

* Node private key

* Harvester private key


# Connecting To The Network

Firstly, open the `Dockerfile` located in the root of this repo, and replace the following with your own values: 

```
ENV harvester_key=<your-key>
ENV boot_key=<your-key>
ENV node_name=<your-chosen-name>
```

Then, simply run docker in the root of this repo: 

```
docker 
```

And your node should be up, running, and connected to the network!
