[![Build Status](https://travis-ci.org/saurabh500/fauxmo.svg?branch=master)](https://travis-ci.org/saurabh500/fauxmo)

# echo
For controlling local devices with the Amazon Echo. This is a clone of the original repository and has config driven device addition features. Add the devices to the [config](https://github.com/saurabh500/fauxmo/blob/master/config.json) with the path to the scripts that can turn devices on or off. 
After configuring, tell Echo "Discover my devices" and all the devices in the config will be added.

Instructions for installation and usage [available on Instructables here](http://www.instructables.com/id/Hacking-the-Amazon-Echo/)

Brought to you by [FabricateIO](http://fabricate.io)

## Quick Start

1. Create a [Python Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
2. git clone *this_repo*
3. cd *this_repo*
4. pip install -r requirements.txt
4. python example-minimal.py
6. Tell Echo, "discover my devices"
7. Use Echo's "turn off device" and "device on" to see True/False script output
