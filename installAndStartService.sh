#!/bin/bash

cp fauxmo.service /lib/systemd/system

systemctl enable fauxmo.service
systemctl start fauxmo.service

