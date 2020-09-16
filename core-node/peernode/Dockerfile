FROM crackthecode01/symbol-deps:0951-broker-patch as builder

ARG BIN_DIR=/usr/src/app/deps/source/catapult-server/_build/bin

WORKDIR /usr/src/app

RUN mkdir -p ./node
EXPOSE 7900 7902

CMD /usr/src/app/deps/source/catapult-server/_build/bin/catapult.server /
