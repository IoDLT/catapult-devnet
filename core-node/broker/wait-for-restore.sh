#!/bin/bash
# wait-for-restore.sh
until [ ! ping -c1 restore &>/dev/null ]; do
    if ! ping -c1 restore &> /dev/null
    then
        echo "RESTORE FINISHED finished!" && /usr/src/app/deps/source/catapult-server/_build/bin/catapult.broker /
        break
    else
        sleep 1
    fi
done