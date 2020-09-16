#!/bin/bash

# Delete any lock files
rm -rf core-node/config/data/*.lock

# Start the node
docker-compose up --build
