#!/bin/sh

# Move config files
sudo cp rabbitmq.conf /etc/rabbitmq/rabbitmq.conf
sudo chown rabbitmq:rabbitmq /etc/rabbitmq/rabbitmq.conf

# Management UI?
sudo rabbitmq-plugins enable rabbitmq_management

# Restart
systemctl restart rabbitmq-server.service