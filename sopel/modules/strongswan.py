# coding=utf8
"""
strongswan.py - Sopel strongSwan channel module with factoids
Copyright 2015, Noel Kuntze
Licensed under the GPLv3

https://strongswan.org
"""

from __future__ import unicode_literals

from sopel import web
import sopel.module
from sopel.config.types import StaticSection, FilenameAttribute
from sopel.logger import get_logger

LOGGER = get_logger(__name__)

import re
import sys
import sqlite3
if sys.version_info.major >= 3:
    unicode = str

"""
	Write variable for database handle
	Write method for initialisation and shutdown to clean up the handle
	Most things to be done is somehow get a connection to a mysql DB up and pull data from there.
"""

""" 
# TODO: finish
# class strongswanSection(StaticSection):
# 	strongswan_db_url = 
"""
entries={ 
	"help" : help,
	"pastebin" : pastebin,
	"documentation" : documentation,
	"obfuscation" : obfuscation,
	"logging" : logging,
	"IDs" : ids
	}

def help(bot, trigger):
	text="If you require help, please state your problem, what you have already tried, "
	text+="your ipsec.conf and complete logs showing the problem. Search through the strongswan-users mailing"
	text+="list's archives. Most problems were discussed on there before."
	if trigger.group(2):
                text=trigger.group(2) + ": " + text
	bot.say(text, 1)	

def logging(bot, trigger):
	text="Please use sane log settings. E.g.: \"mgr=1 ike=1 net=1 enc=0 cfg=2 asn=1 job=1 knl=1\". "
	text+="Try using a file logger with flush_line=yes, to create a discrete log file with strongswan's logs. "
	text+="Refrain from using log level 4."
	if trigger.group(2):
		text=trigger.group(2) + ": " + text
	bot.say(text, 1)

def pastebin(bot, trigger):
	text="Please use a pastebin service, for example bpaste.net, for showing more than two lines."
        if trigger.group(2):
                text=trigger.group(2) + ": " + text
	bot.say(text, 1)

def documentation(bot, trigger):
	text="The project's website provides the documentation to the latest version of StrongSwan."
	if trigger.group(2):
                text=trigger.group(2) + ": " + text
	bot.say(text, 1)

def obfuscation(bot, trigger):
	text="If you need to obfuscate your IP addresses, replace them with addresses of RFC5737."
        if trigger.group(2):
                text=trigger.group(2) + ": " + text
	bot.say(text, 1)

def ids(bot, trigger):
	text="If you are using certificate authentication, then the ID of the participants must be confirmed by its own certificate. "
	text+="This is done by putting it into a SAN. Make sure the ID has a normal format. "
	text+="The human readable type (foo@bar.com for example is an email address) must conform with the type that is set in the certificate."
	text+="E.g.: having foo@bar.com set as ID, but the SAN is "DNS:foo@bar.com" will probably not work. strongSwan also does not parse parts of the DN."
	text+="It only compares the whole DN to the ID and all SAN values to the ID."
	if (trigger.group(2):
		text=trigger.group(2) + ": " + text
	bot.say(text,1)

@rule('\..*')
@example('.pastebin',
	r'Use a pastebin for any text longer than three lines. Do not paste into the channel.',
	re=true

def strongswan(bot,trigger):
	# check if privmsg or in #strongswan
	if trigger.is_privmsg or trigger.sender == "#strongswan":
		searchterm = trigger.group(1)
		if searchterm == "list" and trigger.group(2) == "strongswan":
			bot.say(entries.keys())	
			return
		match=entries[searchterm]
		if match != None:
			match(bot, trigger)
			return
	return
