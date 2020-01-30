#!/bin/bash

cp config.json ../config.json.BAK
# Reset docker images
docker system prune -a
# Reset repo to default
git reset HEAD --hard
# Pull latest
git pull
# copy config back
cp ../config.json.BAK config.json
python3 config.py
echo Ready for starting, now use bash start.sh
echo