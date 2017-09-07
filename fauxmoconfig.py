import json 
from pprint import pprint


class fauxmoconfig():
	def __init__(self, filename):
		with open(filename) as configuration:
			self.configuration = json.load(configuration)
		# Get all DEVICES node
		self.devices = self.configuration['DEVICES']
		# Create a list of fauxmo 
		for device in self.devices:
			print(device)

if __name__ == "__main__":
	fauxmoconfiguration = fauxmoconfig("config.json")
	pprint(fauxmoconfiguration.devices)
