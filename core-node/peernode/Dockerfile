FROM crackthecode01/catapult-deps:v0.9.3.1 as builder

ARG BIN_DIR=/usr/src/app/deps/source/catapult-server/_build/bin

WORKDIR /usr/src/app

RUN mkdir -p ./node
EXPOSE 7900 7902

CMD /usr/src/app/deps/source/catapult-server/_build/bin/catapult.server ./node
