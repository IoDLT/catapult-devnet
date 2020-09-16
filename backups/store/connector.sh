#!/bin/bash
HOME=/root
LOGNAME=root
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
LANG=en_US.UTF-8
SHELL=/bin/bash
PWD=/root

connector-mongodb store \
--mongo /config/db_property.json \
--storj /config/storj_config.json