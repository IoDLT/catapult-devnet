FROM crackthecode01/catapult-deps:keccak-f4 as builder

WORKDIR /usr/src/app

ARG NODE_PATH=/usr/src/app/broker
RUN mkdir -p ${NODE_PATH}

CMD /usr/src/app/deps/source/catapult-server/_build/bin/catapult.broker ./broker