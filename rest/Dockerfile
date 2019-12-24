FROM node:8.16.2-alpine3.10 as builder

ARG REST_PATH=/usr/src/app/rest
ENV HASHING_FUNCTION=keccak

WORKDIR /usr/src/app

RUN apk add --no-cache --update git python python3 gcc build-base zeromq-dev
RUN git clone https://github.com/nemtech/catapult-rest.git rest
WORKDIR ${REST_PATH}

# locking to known working commit
RUN git reset --hard 8eb75b0723b4e1f4d23da6e0495456c4be483610
ADD rest.json ${REST_PATH}/rest/resources/rest.json

RUN chmod 744 ./yarn_setup.sh
RUN ./yarn_setup.sh
RUN mkdir -p /data/db

WORKDIR ${REST_PATH}/rest
RUN yarn rebuild

CMD yarn start resources/rest.json
