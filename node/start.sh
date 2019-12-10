#!/bin/bash

# run config
python3 ./node/config.py $1 $2 $3

# start node
exec /usr/src/app/deps/source/catapult-server/_build/bin/catapult.server /usr/src/app/node

echo Failure.

cat /usr/src/app/node/resources/config-user.properties
