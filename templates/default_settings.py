#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from nx.constants import *

HOSTNAME = socket.gethostname()

## key, value
SITE_SETTINGS = [
    ("seismic_addr" , "224.168.2.8"),
    ("seismic_port" , "42112"),
    ("cache_driver" , "memcached"),
    ("cache_host"   , "192.168.1.50"),
    ("cache_port"   , "11211")
]


## id_folder, title, color, meta_set
## Metaset: tag, required
FOLDERS = [

(1 , "Movies"        , 0x2872B3, 
    [
        ("title",           True),
        ("qc/state",        False),
        ("title/subtitle",  False),
        ("title/original",  False),
        ("title/alternate", False),
        ("description",     False),
        ("identifier/main", False),
        ("role/director",   False),
        ("format",          False),
        ("genre",           False),
        ("subject",         False),
    ]),

(2 , "Series"        , 0x0397BB, 
    [
        ("title",           True),
        ("qc/state",        False),
        ("title/subtitle",  False),
        ("title/original",  False),
        ("title/alternate", False),
        ("description",     False),
        ("identifier/main", True),
        ("role/director",   False),
        ("format",          False),
        ("genre",           False),
        ("subject",         False),
        ("series/season",   True),
        ("series/episode",  True),
    ]),

(3 , "Trailers"      , 0x008E5C, 
    [
        ("title",           True),
        ("qc/state",        True),
        ("identifier/main", True)
    ]),

(4 , "Jingles"       , 0xe0e0e0, 
    [
        ("title",           True)
    ]),

(5 , "Songs"         , 0x8AC91A, 
    [
        ("title",           True),
        ("qc/state",        False),
        ("role/performer",  True),
        ("role/composer",   False),
        ("album",           False),
        ("genre",           True)
    ]),

(6 , "News"          , 0xFE0002, 
    [
        ("title",           True),
        ("qc/state",        False),
        ("title/subtitle",  False),
        ("description",     False),
        ("identifier/main", True),
        ("article",         False),
        ("genre",           False),
        ("subject",         False)
    ]),

(7 , "Fill"          , 0x646464, 
    [
        ("title",           True),
        ("qc/state",        False),
    ]),

(8 , "Templates"     , 0xC7037F, 
    [
        ("title",           True)
    ]),

(9 , "Macros"        , 0x161616, 
    [
        ("title",           True)
    ]),

(10, "Incomming"     , 0xb0b0b0, 
    [
        ("title",           True),
        ("qc/state",        False),
        ("description",     False)
    ]),

(11, "Commercials"   , 0xFFFF01, 
    [
        ("title",           True),
        ("qc/state",        False),
        ("identifier/main", True),
        ("commercials/client", True)
    ]),

(12, "Teleshopping"  , 0xFFC700, 
    [
        ("title",           True),
        ("qc/state",        False),
        ("identifier/main", True),
        ("commercials/client", True),
    ])
]







## id_storage, title, protocol, path, login, password
STORAGES = [
(1, "nxcore", CIFS, "//192.168.1.50/share", "nebula", "nebula"),
]

## agent, title, host, autostart, loop_delay, settings
SERVICES = [
("meta",   "Meta"  , HOSTNAME, 1, 5 ,"""<settings></settings>"""),
("hive",   "Hive"  , HOSTNAME, 1, 5 ,"""<settings></settings>"""),
("broker", "Broker", HOSTNAME, 1, 10 ,"""<settings></settings>"""),
("conv",   "Conv",   HOSTNAME, 1, 10 ,"""<settings></settings>""")
]


#id_action, title, config
ACTIONS = []

