#!/usr/bin/python
# ____                        _             __  __ _ _ _         _   
#|  _ \ ___  ___ ___  _ __   | |__  _   _  |  \/  (_) | | ____ _| |_ 
#| |_) / _ \/ __/ _ \| '_ \  | '_ \| | | | | |\/| | | | |/ / _` | __|
#|  _ <  __/ (_| (_) | | | | | |_) | |_| | | |  | | | |   < (_| | |_ 
#|_| \_\___|\___\___/|_| |_| |_.__/ \__, | |_|  |_|_|_|_|\_\__,_|\__|
#                                   |___/                            
#
#
#/*******************************************************
# * Copyright (C) 2016 Milkat milkat@anonymousspeech.com
# * 
# * This script has been made by Milkat.
# * 
# * Recon can not be copied and/or distributed without the express
# * permission of Milkat
# *******************************************************/

import logging
import argparse
import subprocess

def initLogging( args ):
    formatString = '[%(levelname)s][%(asctime)s] : %(message)s' # specify a format string
    logLevel = logging.INFO # specify standard log level
    logging.basicConfig( format=formatString , level=logLevel, datefmt='%Y-%m-%d %I:%M:%S')
    log_file = args.output
    fileHandler = logging.FileHandler( log_file )
    logging.root.addHandler( fileHandler ) # add file handler to logging

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='       Add here the url you want to use. Example: www.google.com')
parser.add_argument('-o', '--output', help='    Add here the output file for logging')
args = parser.parse_args()
initLogging( args )

fierce = "fierce -dns "+args.url
nmap = "nmap -O -sS -sV -Pn "+args.url
dmitry = "dmitry -winsepfb "+args.url
line = "---------------------------------------------------------------------------------------------------------"
url = args.url
url2 = url.replace("www.", "", 1)
dnsmap = "dnsmap "+url2
dnsrecon = "dnsrecon -d "+url2

print line
print "Doing a fierce dns scan now, please hold on, this can take a while"
print line
p = subprocess.Popen( fierce, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
stdout_string , stderr_string = p.communicate()

logging.info( stderr_string )
logging.info( stdout_string )
print line
print "That where the results"
print line
print "Now an nmap will save the day"
print line
p = subprocess.Popen( nmap, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
stdout_string, stderr_string = p.communicate()

logging.info( stderr_string )
logging.info( stdout_string )
print line
print "Thank you Nmap, lets go on"
print line
print "Now let's see what DMitry tells us"
print line

p = subprocess.Popen( dmitry, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
stdout_string, stderr_string = p.communicate()

logging.info( stderr_string )
logging.info( stdout_string )

print line
print "DMitry was wise as usual"
print line
print "Let's make a dnsmap"
print line

p = subprocess.Popen( dnsmap, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
stdout_string, stderr_string = p.communicate()

logging.info( stderr_string )
logging.info( stdout_string )

print line
print "And even more DNS info"
print "Digging NOW"
print line

p = subprocess.Popen( dnsrecon, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
stdout_string, stderr_string = p.communicate()

logging.info( stderr_string )
logging.info( stdout_string )

print line
print "That's it! That is all the info we can find, happy hacking!!!!"
print line
