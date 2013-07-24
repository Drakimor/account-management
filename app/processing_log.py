#!/usr/bin/env python

import csv
import os
import logging
import logging.handlers
from pprint import PrettyPrinter
from socket import gethostname
from datetime import datetime
from time import strftime

logging.EMAIL = (logging.INFO+logging.WARNING)>>1

class process_log(object):
	__slots__ = ['__logger', '__pretty']

	def __init__(self, name):
		# set up nice printer
		self.__pretty = PrettyPrinter()
		#set up log file name
		log_filename = "/var/log/greenscreen/%s"% name
		# create logger
		self.__logger = logging.getLogger("Greenscreen")
		self.__logger.setLevel(logging.DEBUG)
#		self.__logger.addLevelName(logging.EMAIL, "email")
		# Add the log message handler to the logger
		file_handler = logging.handlers.RotatingFileHandler(log_filename, maxBytes=20971520, backupCount=5)
		formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s","%Y-%m-%d %H:%M:%S")
		file_handler.setFormatter(formatter)
		file_handler.setLevel(logging.DEBUG)
#		file_handler.addLevelName(logging.EMAIL, "email")
		self.__logger.addHandler(file_handler)
		
		mailhost = "mx.tribalbrands.mobi"
		fromaddr = "GS Processing <gs@tribaltech.com>"
		toaddrs = ["jonathan@tribaltech.com"]
		subject = "GS Error on %s"% gethostname().split('.')[0]
		credentials = None
		smtp_handler = logging.handlers.SMTPHandler(mailhost, fromaddr, toaddrs, subject, credentials)
		smtp_handler.setFormatter(formatter)
#		smtp_handler.addLevelName(logging.EMAIL, "email")
		smtp_handler.setLevel(logging.ERROR)
		self.__logger.addHandler(smtp_handler)
		
		self.__logger.debug("="*80)
		self.__logger.debug("  Starting run  ".center(80, "="))
		self.__logger.debug("="*80)

	def email(self, message, pretty=False):
		if pretty == True: message = self.__pretty.pformat(message)
		self.__logger.log(logging.EMAIL, message)
	def debug(self, message, pretty=False):
		if pretty == True: message = self.__pretty.pformat(message)
		self.__logger.debug(message)
	def info(self, message, pretty=False):
		if pretty == True: message = self.__pretty.pformat(message)
		self.__logger.info(message)
	def warn(self, message, pretty=False):
		if pretty == True: message = self.__pretty.pformat(message)
		self.__logger.warn(message)
	def error(self, message, pretty=False):
		if pretty == True: message = self.__pretty.pformat(message)
		self.__logger.error(message)
	def critical(self, message, pretty=False):
		if pretty == True: message = self.__pretty.pformat(message)
		self.__logger.critical(message)
