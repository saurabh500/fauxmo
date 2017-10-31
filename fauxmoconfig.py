import json 
import logging
from pprint import pprint


class fauxmoconfig():
	def __init__(self, filename):
		logging.debug("Loading log from " + filename)
		with open(filename) as configuration:
			self.configuration = json.load(configuration)
		# Get all DEVICES node
		self.devices = self.configuration['DEVICES']
		# Create a list of fauxmo 
		for device in self.devices:
			print(device)

if __name__ == "__main__":
	fauxmoconfiguration = fauxmoconfig(os.path.realpath("config.json"))
	pprint(fauxmoconfiguration.devices)
