FROM crackthecode01/catapult-deps:v0.9.5.1 as builder

WORKDIR /usr/src/app

ARG NODE_PATH=/usr/src/app/broker
RUN mkdir -p ${NODE_PATH}

CMD /usr/src/app/deps/source/catapult-server/_build/bin/catapult.broker /