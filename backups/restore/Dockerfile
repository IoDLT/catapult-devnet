FROM golang:1.15.0
# Copy project files
WORKDIR /src
RUN git clone https://github.com/CrackTheCode016/connector-mongodb --single-branch --branch no-auth connector
RUN ls 
WORKDIR /src/connector
# Build
RUN go build
RUN cp ./connector-mongodb /bin/connector-mongodb

FROM ubuntu:latest

RUN apt update && apt -y install mongodb
COPY --from=0 /bin/connector-mongodb /bin/connector-mongodb

WORKDIR /usr/src/app
COPY restore.sh restore.sh
COPY mongo.js mongo.js
RUN chmod +x restore.sh

# Run the command on container startup
CMD bash restore.sh