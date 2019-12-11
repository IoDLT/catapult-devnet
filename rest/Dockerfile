FROM node:8.16.2-alpine3.10 as builder

ARG REST_PATH=/usr/src/app/rest
ARG API_KEY=9C6EEEB66C3BA58E6C0B16220106E13010D29DE6106FC678201045EA5AE8752C

WORKDIR /usr/src/app

# RUN apt-get update && apt-get install -y git
RUN apk add --no-cache --update git python python3 gcc build-base zeromq-dev
RUN git clone https://github.com/Alexhuszagh/catapult-rest.git rest
ADD config.py ${REST_PATH}/rest
RUN chmod 744 ${REST_PATH}/rest/config.py

WORKDIR ${REST_PATH}
RUN pwd
RUN chmod 744 ./yarn_setup.sh
RUN ./yarn_setup.sh
RUN mkdir -p /data/db

WORKDIR ${REST_PATH}/rest
RUN yarn rebuild
RUN python3 config.py ${API_KEY}

CMD yarn start resources/rest.json