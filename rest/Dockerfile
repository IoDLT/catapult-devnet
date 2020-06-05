FROM node:12.18.0-alpine3.10 as builder

ARG REST_PATH=/usr/src/app/rest

WORKDIR /usr/src/app

RUN apk add --no-cache --update git python python3 gcc build-base zeromq-dev
RUN git clone https://github.com/nemtech/catapult-rest.git --branch task/vrf-lock rest
WORKDIR ${REST_PATH}
ADD rest.json ${REST_PATH}/rest/resources/rest.json

RUN chmod 744 ./yarn_setup.sh
RUN ./yarn_setup.sh
RUN mkdir -p /data/db

WORKDIR ${REST_PATH}/rest
RUN yarn rebuild

CMD yarn start resources/rest.json
