#!/bin/bash

pushd ..
pip install -r requirements.txt

cp fauxmo.service /lib/systemd/system

systemctl enable fauxmo.service
systemctl start fauxmo.service

popd

