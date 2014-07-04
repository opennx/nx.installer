#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nx import *
from optparse import OptionParser


NX_ROOT = os.path.split(sys.argv[0])[0]
if not NX_ROOT in sys.path:
    sys.path.append(NX_ROOT)

from template.actions import *
from template.folders import *
from template.metadata import *
from template.services import *
from template.site_settings import *
from template.storages import *


usage = "usage: %prog [options]"
parser = OptionParser(usage)

parser.add_option("-s", "--structure", dest="structure",
                      help="(re)create database structure", 
                      action="store_true"
                      )

parser.add_option("-o", "--objects", dest="objects",
                      help="Truncate objects and meta tables", 
                      action="store_true"
                      )

(options, args) = parser.parse_args()


db = DB()


##############################################################  
## create db structure

if options.structure:
    print ("Recreating database structure")
    for q in DB_TEMPLATE:
        db.query(q)
    db.commit()
    
## create db structure
##############################################################
## metadata set

if not options.structure:
    if options.objects:
        print ("Removing objects")
        db.query("TRUNCATE TABLE nx_assets, nx_meta, nx_items, nx_bins, nx_events RESTART IDENTITY")
        db.commit()



print "Installing metadata structure"
db.query("TRUNCATE TABLE nx_meta_types, nx_meta_aliases RESTART IDENTITY")
for ns, tag, editable, searchable, class_, default, settings in BASE_META_SET:
    q = """INSERT INTO nx_meta_types (namespace, tag, editable, searchable, class, default_value, settings) VALUES ('%s' ,'%s', %d, %d, %d, '%s', '%s')""" % \
           (ns, tag, editable, searchable, class_, default, json.dumps(settings))
    db.query(q)
db.commit()

for tag, lang, alias, col_header in META_ALIASES:
    q = """INSERT INTO nx_meta_aliases (tag, lang, alias, col_header) VALUES ('%s' ,'%s', '%s', '%s')""" % (tag, lang, alias, col_header)
    db.query(q)
db.commit()



db.query("TRUNCATE TABLE nx_settings, nx_folders, nx_services, nx_storages RESTART IDENTITY")

print "Installing site settings"
for key, value in SITE_SETTINGS:
    q = """INSERT INTO nx_settings(key,value) VALUES ('%s','%s')""" % (key, value)
    db.query(q)
db.commit()

print "Installing folders"
for id_folder, title, color, meta_set in FOLDERS:
  q = "INSERT INTO nx_folders (id_folder, title, color, meta_set) VALUES (%d,'%s',%d, '%s')" % (id_folder, title, color, json.dumps(meta_set))
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
