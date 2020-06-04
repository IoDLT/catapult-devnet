#!/bin/bash

# backup config
cp config.json /tmp/config.json.BAK
# Reset docker images
docker system prune -a
# Reset repo to default
git reset HEAD --hard

# Make sure data is reset
source utils/reset_node.sh

# Pull latest
git pull

# copy config back
cp /tmp/config.json.BAK config.json

python3 config.py

echo Ready for generating the certificate (bash utils/generate_certificate.sh)
echo