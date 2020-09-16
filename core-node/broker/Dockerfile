FROM crackthecode01/symbol-deps:0951-broker-patch as builder

WORKDIR /usr/src/app

ARG NODE_PATH=/usr/src/app/broker
RUN mkdir -p ${NODE_PATH}
RUN apt update -y && apt install iputils-ping -y
ADD wait-for-restore.sh .
RUN chmod 744 wait-for-restore.sh

CMD ./wait-for-restore.sh
