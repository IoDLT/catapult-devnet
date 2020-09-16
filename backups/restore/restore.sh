#!/bin/bash

dump_dir=/usr/src/app
host=172.28.1.2

connector-mongodb restore \
--latest \
--match catapult \
--path nodebackup/ \
--storj /config/storj_config.json

mongo --host ${host} mongo.js
mongorestore --host ${host} -d catapult -c transactionStatements ${dump_dir}/dump/catapult.bson/transactionStatements.bson
mongorestore --host ${host} -d catapult -c transactions ${dump_dir}/dump/catapult.bson/transactions.bson
mongorestore --host ${host} -d catapult -c namespaces ${dump_dir}/dump/catapult.bson/namespaces.bson
mongorestore --host ${host} -d catapult -c mosaics ${dump_dir}/dump/catapult.bson/mosaics.bson
mongorestore --host ${host} -d catapult -c mosaicResolutionStatements ${dump_dir}/dump/catapult.bson/mosaicResolutionStatements.bson
mongorestore --host ${host} -d catapult -c chainStatistic ${dump_dir}/dump/catapult.bson/chainStatistic.bson
mongorestore --host ${host} -d catapult -c blocks ${dump_dir}/dump/catapult.bson/blocks.bson
mongorestore --host ${host} -d catapult -c accounts ${dump_dir}/dump/catapult.bson/accounts.bson
