#!/bin/bash

# backup config
cp config.json /tmp/config.json.BAK
# Reset docker images
docker system prune -a
# Reset repo to default
git reset HEAD --hard

# Make sure data is reset
source reset_node.sh

# Pull latest
git pull

# copy config back
cp /tmp/config.json.BAK config.json

python3 config.py
echo Ready for starting, now use bash start.sh
echo