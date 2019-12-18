FROM crackthecode01/catapult-deps:latest as builder

ARG BIN_DIR=/usr/src/app/deps/source/catapult-server/_build/bin

WORKDIR /usr/src/app

RUN mkdir -p ./node
EXPOSE 7900 7902

CMD ls /data && /usr/src/app/deps/source/catapult-server/_build/bin/catapult.server ./node
