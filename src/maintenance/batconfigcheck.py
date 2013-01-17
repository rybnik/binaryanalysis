#!/usr/bin/python

## Binary Analysis Tool
## Copyright 2013 Armijn Hemel for Tjaldur Software Governance Solutions
## Licensed under Apache 2.0, see LICENSE file for details

'''
This script can be used to check the validity of the BAT configuration file. It
specifically is used to check the validity of databases for the ranking scan.
'''

import os, sys, sqlite3
from optparse import OptionParser
import ConfigParser

## Check if this has been defined for file2package
## * BAT_PACKAGE

## Check if any of these have been defined for ranking and check database
## schemas, whether it is the old or new format, etc.
## * BAT_AVG_C
## * BAT_AVG_JAVA
## * BAT_AVG_C#
## * BAT_AVG_ACTIONSCRIPT
## * BAT_CLONE_DB
## * BAT_DB
## * BAT_FUNCTIONNAMECACHE_C
## * BAT_FUNCTIONNAMECACHE_JAVA
## * BAT_LICENSE_DB
## * BAT_STRINGSCACHE_C
## * BAT_STRINGSCACHE_JAVA
## * BAT_STRINGSCACHE_C#
## * BAT_STRINGSCACHE_ACTIONSCRIPT

## Check if any of these have been defined in any of the postrunscans
## * BAT_REPORTDIR
## * storedir

def main(argv):
	pass

if __name__ == "__main__":
	main(sys.argv)