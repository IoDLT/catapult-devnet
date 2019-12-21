FROM node:8.16.2-alpine3.10 as builder

ARG REST_PATH=/usr/src/app/rest
ENV HASHING_FUNCTION=keccak

WORKDIR /usr/src/app

RUN apk add --no-cache --update git python python3 gcc build-base zeromq-dev
RUN git clone https://github.com/Alexhuszagh/catapult-rest.git rest
ADD rest.json ${REST_PATH}/rest/resources/rest.json

WORKDIR ${REST_PATH}
RUN pwd
RUN chmod 744 ./yarn_setup.sh
RUN ./yarn_setup.sh
RUN mkdir -p /data/db

WORKDIR ${REST_PATH}/rest
RUN yarn rebuild

CMD yarn start resources/rest.json
