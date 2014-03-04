#!/usr/bin/env python
# -*- coding: utf-8 -*-

DEBUG = True

if DEBUG:
    import socket
    HOSTNAME = socket.gethostname()

from nx.constants import *


## key, value
SITE_SETTINGS = [
    ("seismic_addr" , "224.168.2.8"),
    ("seismic_port" , "42112"),
    ("cache_driver" , "memcached"),
    ("cache_host"   , "localhost"),
    ("cache_port"   , "11211")
]

## id_folder, title, color
FOLDERS = [
(1, "Music video" , 0xe34931),
(2, "Music"       , 0xe34931),
(3, "Movies"      , 0x019875),
(4, "Short films" , 0x019875),
(5, "Series"      , 0x009706),
(6, "Jingles"     , 0xeec050),
(7, "Templates"   , 0x5b5da7),
(8, "Trailers"    , 0x9c2336),
(9, "Macros"      , 0xd2c5bb),
(11,"Incomming"   , 0x20b9eb),
(12,"News"        , 0x0066cc)
]

## agent, title, host, autostart, loop_delay, settings
SERVICES = [
("meta" , "Meta"  , HOSTNAME, 1, 5 ,"""<settings></settings>"""),
("admin", "Admin" , HOSTNAME, 1, 5 ,"""<settings></settings>"""),
("hive",  "Hive"  , HOSTNAME, 1, 5 ,"""<settings></settings>"""),
("watch", "Watch" , HOSTNAME, 1, 10,
"""
<settings>

    <mirror>
         <id_storage>2</id_storage>
         <path>Acquisition/Movies</path>
         <recursive>1</recursive>
         <meta tag='origin'>Acquisition</meta>
         <meta tag='id_folder'>3</meta>
     </mirror>

    <mirror>
         <id_storage>2</id_storage>
         <path>Acquisition/Music</path>
         <recursive>1</recursive>
         <filters>
              <filter>audio</filter>
         </filters> 
         <meta tag='origin'>Acquisition</meta>
         <meta tag='id_folder'>2</meta>
     </mirror>

    <mirror>
         <id_storage>2</id_storage>
         <path>Acquisition/Youtube</path>
         <recursive>0</recursive>
         <filters>
              <filter>video</filter>
         </filters> 
         <meta tag='origin'>Acquisition</meta>
         <meta tag='id_folder'>11</meta>
         <post><![CDATA[
aid = os.path.splitext(os.path.basename(apath))[0]
if len(aid) == 11:
    asset["source"] = "Youtube"
    asset["identifier/youtube"] = asset["title"]
else:
    failed = True
]]>
         </post>
     </mirror>

    <mirror>
         <id_storage>2</id_storage>
         <path>Acquisition/Vimeo</path>
         <recursive>0</recursive>
         <filters>
              <filter>video</filter>
         </filters> 
         <meta tag='origin'>Acquisition</meta>
         <meta tag='id_folder'>11</meta>
         <post><![CDATA[
aid = os.path.splitext(os.path.basename(apath))[0]
if aid.isdigit():
    asset["source"] = "Vimeo"
    asset["identifier/vimeo"] = aid
else:
    failed = True

]]>
         </post>
     </mirror>




    <mirror>
        <id_storage>2</id_storage>
        <path>Library/Jingles</path>
        <recursive>0</recursive>
        <meta tag='origin'>Library</meta>
        <meta tag='id_folder'>6</meta>
    </mirror>
    <mirror>
        <id_storage>2</id_storage>
        <path>Library/Templates</path>
        <recursive>0</recursive>
        <meta tag='origin'>Library</meta>
        <meta tag='id_folder'>7</meta>
    </mirror>
    <mirror>
        <id_storage>2</id_storage>
        <path>Library/Trailers</path>
        <recursive>0</recursive>
        <meta tag='origin'>Library</meta>
        <meta tag='id_folder'>8</meta>
    </mirror>
</settings>
""")

]

## id_storage, title, protocol, path, login, password
STORAGES = [
(1, "nxcore", CIFS, "//nxcore/nxcore", "nebula", "nebula"),
(2, "nxstor", CIFS, "//nxcore/nxstor", "nebula", "nebula")
]
