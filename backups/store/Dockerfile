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

RUN apt update && apt -y install cron

COPY --from=0 /bin/connector-mongodb /bin/connector-mongodb

# Copy hello-cron file to the cron.d directory
COPY cron /etc/cron.d/cron

COPY connector.sh /usr/bin/store-command-connector.sh
RUN chmod +x /usr/bin/store-command-connector.sh

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cron

# Apply cron job
RUN crontab /etc/cron.d/cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log