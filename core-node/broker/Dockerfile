FROM crackthecode01/catapult-deps:latest as builder
ARG NODE_PATH=/usr/src/app/broker
RUN mkdir -p ${NODE_PATH}
WORKDIR ${NODE_PATH}
ADD ./resources ${NODE_PATH}/resources
CMD /usr/src/app/deps/source/catapult-server/_build/bin/catapult.broker .