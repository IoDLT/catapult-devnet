from ubuntu:18.04

WORKDIR /usr/src/app
RUN mkdir -p rest && cd rest/ && git clone https://github.com/nemtech/catapult-rest.git
RUN cd catapult-rest/ 
RUN ./yarn-setup.sh

CMD yarn start resources/rest.json