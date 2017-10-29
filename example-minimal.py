#!/usr/bin/python
""" fauxmo_minimal.py - Fabricate.IO

    This is a demo python file showing what can be done with the debounce_handler.
    The handler prints True when you say "Alexa, device on" and False when you say
    "Alexa, device off".

    If you have two or more Echos, it only handles the one that hears you more clearly.
    You can have an Echo per room and not worry about your handlers triggering for
    those other rooms.

    The IP of the triggering Echo is also passed into the act() function, so you can
    do different things based on which Echo triggered the handler.
"""

import fauxmo
import logging
import time
import os
import sys
import fauxmoconfig
import argparse
from debounce_handler import debounce_handler

#logging.basicConfig(level=logging.DEBUG, filename="/var/log/example-minimal.py",
#	format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


class device_handler(debounce_handler):
    """Publishes the on/off state requested,
       and the IP address of the Echo making the request.
    """
    TRIGGERS = {"TV": 52000, "Light" : 53000}

    def __init__(self, name, port, on_command, off_command):
        super(device_handler, self).__init__()
        self.name = name
        self.port = port
	self.on_command = on_command
	self.off_command = off_command

    def act(self, client_address, state):
        if state == True:
	    os.system(self.on_command)
            print "State", state, "from client @", client_address
            return True
	if state == False:
	    os.system(self.off_command)
	    print "State", state, "from client @", client_address
	    return True

def parse_command_line():
    parser = argparse.ArgumentParser(description='Pass parameters for fauxmo')
    parser.add_argument('--test', default=False, const=True, action='store_const', help="Pass as a parameter if the service should be run in test mode")
    parser.add_argument('--config', default="/home/pi/fauxmo/config.json", help="Specify the path of the config file")
    arguments = parser.parse_args()
    return arguments

if __name__ == "__main__":
    # Parse command line arguments 
    arguments = parse_command_line()
    isTestMode = arguments.test
    logFileName = "/var/log/fauxmo.log"
    if isTestMode : 
	logFileName = "./test.log"
    logging.basicConfig(level=logging.DEBUG, filename=logFileName, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Startup the fauxmo server
    print("Starting the server")
    fauxmo.DEBUG = True
    p = fauxmo.poller()
    u = fauxmo.upnp_broadcast_responder()
    configuration = fauxmoconfig.fauxmoconfig(os.path.realpath("config.json"))
    print("About to initialize socket")
    u.init_socket()
    p.add(u)
    print("Socket initialized and added to poller")

    # Register the device callback as a fauxmo handler
    # d = device_handler()
    print("Registering the device Call Back ")
    for device in configuration.devices:
	handler = device_handler(device["name"], device["port"], device["on_cmd"], device["off_cmd"])
	fauxmo.fauxmo(device["name"], u, p, None, device["port"], handler)

    logging.debug("Entering fauxmo polling loop")
    print("Entering the faxmo polling loop")
    while True:
        try:
            # Allow time for a ctrl-c to stop the process
	    p.poll(100)
            time.sleep(0.1)
	    if isTestMode : 
		break;
        except Exception, e:
            logging.critical("Critical exception: " + str(e))
	    logging.debug("Exception encountered " + str(e))
            break
    logging.debug("Exit the Application")
