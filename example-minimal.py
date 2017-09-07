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

from debounce_handler import debounce_handler

logging.basicConfig(level=logging.DEBUG, filename="/var/log/example-minimal.py",
	format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


class device_handler(debounce_handler):
    """Publishes the on/off state requested,
       and the IP address of the Echo making the request.
    """
    TRIGGERS = {"TV": 52000, "Light" : 53000}

    def __init__(self, name, port):
        super(device_handler, self).__init__()
        self.name = name
        self.port = port

    def act(self, client_address, state):
        if self.name == "TV":
            os.system("irsend SEND_ONCE SAMSUNG55 KEY_POWER");
            print "State", state, "from client @", client_address
            return True
        if self.name == "Light" and state == True:
            os.system("/home/pi/gitclone/echo/echo-master/lightson.sh")
            print "Turning light on"
            return True
        if self.name == "Light" and state == False:
            os.system("/home/pi/gitclone/echo/echo-master/lightsoff.sh")
            print "Turning light off"
            return True
        if self.name == "Living" and state == True:
            os.system("/home/pi/gitclone/echo/echo-master/lightson.sh")
            os.system("irsend SEND_ONCE SAMSUNG55 KEY_POWER");
            print "Turning light on"
            return True
        if self.name == "Living" and state == False:
            os.system("/home/pi/gitclone/echo/echo-master/lightsoff.sh")
            os.system("irsend SEND_ONCE SAMSUNG55 KEY_POWER");
            print "Turning light off"
            return True
        
if __name__ == "__main__":
    # Startup the fauxmo server
    print("Starting the server")
    fauxmo.DEBUG = True
    p = fauxmo.poller()
    u = fauxmo.upnp_broadcast_responder()
    print("About to initialize socket")
    u.init_socket()
    p.add(u)
    print("Socket initialized and added to poller")

    # Register the device callback as a fauxmo handler
    # d = device_handler()
    print("Registering the device Call Back ")
    tv = device_handler("TV", 53000)
    lights = device_handler("Light", 54000)
    living = device_handler("Living", 55000)
    fauxmo.fauxmo("TV", u, p, None, 53000, tv)
    fauxmo.fauxmo("Light", u, p, None, 54000, lights)
    fauxmo.fauxmo("Living", u, p, None, 55000, living)
    
    #for trig, port in d.TRIGGERS.items():
    #    fauxmo.fauxmo(trig, u, p, None, port, d)

    # Loop and poll for incoming Echo requests
    logging.debug("Entering fauxmo polling loop")
    print("Entering the faxmo polling loop")
    while True:
        try:
            # Allow time for a ctrl-c to stop the process
	    p.poll(100)
            time.sleep(0.1)
        except Exception, e:
            logging.critical("Critical exception: " + str(e))
	    logging.debug("Exception encountered " + str(e))
            break
    logging.debug("Exit the Application")
