#!/bin/bash

pip install -r requirements

cp fauxmo.service /lib/systemd/system

systemctl enable fauxmo.service
systemctl start fauxmo.service

