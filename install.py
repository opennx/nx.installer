#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from nx.server import *

NX_ROOT = os.path.split(sys.argv[0])[0]
if not NX_ROOT in sys.path:
    sys.path.append(NX_ROOT)


from templates.default_db import *
from templates.default_meta import *
from templates.default_settings import *


##############################################################  
## create db structure

#if os.path.exists(".cache"):
#    try:    os.remove(".cache")
#    except: pass

#if os.path.exists(config["db_host"]):
#    try:    os.remove(config["db_host"])
#    except: critical_error("Unable to remove old DB File")

db = DB()
#for q in SQLITE_TPL:
#    db.query(q)
#b.commit()

#if config['db_driver'] == "postgres":
#    try: db.query("create extension unaccent;")
#    except: pass

## create db structure
##############################################################
## metadata set

print "Truncating old tables"
db.query("TRUNCATE TABLE nx_assets, nx_meta, nx_items, nx_bins, nx_events RESTART IDENTITY")
db.query("TRUNCATE TABLE nx_meta_types, nx_meta_aliases RESTART IDENTITY")
db.commit()


print "Installing meta types"
for ns, tag, editable, searchable, class_, default, settings in BASE_META_SET:
    q = """INSERT INTO nx_meta_types (namespace, tag, editable, searchable, class, default_value, settings) VALUES ('%s' ,'%s', %d, %d, %d, '%s', '%s')""" % \
           (ns, tag, editable, searchable, class_, default, json.dumps(settings))
    db.query(q)
db.commit()

print "Installing meta aliases"
for tag, lang, alias, col_header in META_ALIASES:
    q = """INSERT INTO nx_meta_aliases (tag, lang, alias, col_header) VALUES ('%s' ,'%s', '%s', '%s')""" % (tag, lang, alias, col_header)
    db.query(q)
db.commit()





sys.exit(0)

db.query("TRUNCATE TABLE nx_meta_types, nx_meta_aliases, nx_settings, nx_folders, nx_services, nx_storages RESTART IDENTITY")

print "Installing site settings"
for key, value in SITE_SETTINGS:
    q = """INSERT INTO nx_settings(key,value) VALUES ('%s','%s')""" % (key, value)
    db.query(q)
db.commit()

print "Installing folders"
for id_folder, title, color in FOLDERS:
  q = "INSERT INTO nx_folders (id_folder, title, color) VALUES (%d,'%s',%d)" % (id_folder, title, color)
  db.query(q)
db.commit()

print "Installing services"
for agent, title, host, autostart, loop_delay, settings in SERVICES:
    q = "INSERT INTO nx_services (agent, title, host, autostart, loop_delay, settings, state, pid, last_seen) VALUES ('%s','%s','%s',%d, %d, '%s',0,0,0)" % \
        (agent, title, host, autostart, loop_delay, db.sanit(settings))
    db.query(q)
db.commit()

print "Installing storages"
for id_storage, title, protocol, path, login, password in STORAGES:
    q = "INSERT INTO nx_storages (id_storage, title, protocol, path, login, password) VALUES (%d, '%s', %d, '%s', '%s', '%s')" % \
        (id_storage, db.sanit(title), protocol, db.sanit(path), db.sanit(login), db.sanit(password))
    db.query(q)
db.commit() 