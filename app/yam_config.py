#!/usr/bin/env python

from ConfigParser import ConfigParser

conf_file = "/etc/YamConf/provisionie.properties"
sections = ['auth','server']

def get_conf():
	conf_values = {}
	config = ConfigParser()
	config.read(conf_file)
	for section in sections:
		if section not in conf_values:
			conf_values[section] = {}
		items = config.items(section)
		for item in items:
			conf_values[section][item[0]] = item[1]
	return conf_values

if __name__ == "__main__":
	from pprint import PrettyPrinter
	pretty = PrettyPrinter()
	pretty.pprint(get_conf())
