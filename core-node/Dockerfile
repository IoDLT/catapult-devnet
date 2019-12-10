FROM crackthecode01/catapult-deps:latest as builder

ARG NODE_PATH=/usr/src/app/node
ARG BIN_DIR=/usr/src/app/deps/source/catapult-server/_build/bin

ARG harvester_key=D1546BA67402AB1834C8350B6400102D4503D3A56109EFDCF967A83AE3294498
ARG boot_key=7D9920759103138AD68D5371787CDB4BC0921DA71039A226E909C54E3BF88115
ARG node_name=friendly

# copy node files, start node
WORKDIR /usr/src/app
RUN mkdir -p ${NODE_PATH} 
RUN cd ./node
ADD node/ ${NODE_PATH}
RUN chmod 744 ./node/start.sh 
RUN chmod 744 ./node/config.py
RUN python3 ./node/config.py "$harvester_key" "$boot_key" "$node_name"

EXPOSE 7900 7902

# CMD ./node/start.sh $harvester_key $boot_key $node_name
CMD /usr/src/app/deps/source/catapult-server/_build/bin/catapult.server ./node \
    && /usr/src/app/deps/source/catapult-server/_build/bin/catapult.broker