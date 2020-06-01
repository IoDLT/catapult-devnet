FROM node:8.16.2-alpine3.10 as builder

ARG REST_PATH=/usr/src/app/rest

WORKDIR /usr/src/app

RUN apk add --no-cache --update git python python3 gcc build-base zeromq-dev
RUN git clone https://github.com/nemtech/catapult-rest.git rest 

WORKDIR ${REST_PATH}
# lock at commit
RUN git checkout ccb30c1b727f02a613a7d68e98ff01aa397a75bb
ADD rest.json ${REST_PATH}/rest/resources/rest.json

RUN chmod 744 ./yarn_setup.sh
RUN ./yarn_setup.sh
RUN mkdir -p /data/db

WORKDIR ${REST_PATH}/rest
RUN yarn rebuild

CMD yarn start resources/rest.json
