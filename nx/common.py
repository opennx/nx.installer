#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import socket
import json
import time

from xml.etree import ElementTree as ET
from constants import *

if __name__ == "__main__":
    sys.exit(-1)

if sys.platform == "win32":
    PLATFORM   = "windows"
    python_cmd = "c:\\python27\python.exe"
else:
    PLATFORM   = "linux"
    python_cmd = "python"

HOSTNAME = socket.gethostname()

def critical_error(message):
    try: 
        logging.error(message)
    except: 
        print "CRITICAL ERROR: %s" % message
    sys.exit(-1)

########################################################################
## Config

class Config(dict):
    def __init__(self):
        super(Config, self).__init__()
        self["host"] = socket.gethostname()  # Machine hostname
        self["user"] = "Core"                # Service identifier. Should be overwritten by service/script.
        try:
            local_settings = json.loads(open("local_settings.json").read())
        except:
            critical_error("Unable to open site_settings file.")
        self.update(local_settings)

    def __getitem__(self,key):
        return self.get(key,False)

config = Config()

## Config
########################################################################
## Messaging
#
# Seismic messaging sends multicast UDP message over local network. 
# It's useful for logging, updating client views, configurations etc.
#

class Messaging():
    def __init__(self):
        self.init()

    def init(self):
        self.MCAST_ADDR = config["seismic_addr"]
        self.MCAST_PORT = int(config["seismic_port"])
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
  
    def send(self, method, data=None):
        """
        message = [timestamp, site_name, host, method, DATA] 
        """        
        self.sock.sendto(json.dumps([time.time(), config["site_name"], config["host"], method, data]), (self.MCAST_ADDR,self.MCAST_PORT) )

messaging = Messaging()

## Messaging
########################################################################
## Logging

class Logging():
    def __init__(self):
        pass

    def _send(self,msgtype,message):
        try:
            print msgtype.ljust(10), config['user'].ljust(15), message
        except:
            print message.encode("utf-8")
        messaging.send("LOG",[config['user'], msgtype, message])

    def debug   (self,msg): self._send("DEBUG",msg) 
    def info    (self,msg): self._send("INFO",msg) 
    def warning (self,msg): self._send("WARNING",msg) 
    def error   (self,msg): self._send("ERROR",msg) 
    def goodnews(self,msg): self._send("GOOD NEWS",msg) 

logging   = Logging()  

## Logging
########################################################################
## Filesystem

class Storage():
    pass

class Storages(dict):
    def __init__(self):
        super(Storages, self).__init__()

storages  = Storages()

## Filesystem
########################################################################