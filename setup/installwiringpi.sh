#!/bin/bash

git clone git://git.drogon.net/wiringPi
pushd wiringPi
git pull origin
./build

popd 
rm -rf wiringPi

