#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nx import *
from optparse import OptionParser

NX_ROOT = os.path.split(sys.argv[0])[0]
if not NX_ROOT in sys.path:
    sys.path.append(NX_ROOT)

from db_structure import DB_STRUCTURE

from default.actions import ACTIONS
from default.channels import CHANNELS
from default.folders import FOLDERS
from default.metadata import BASE_META_SET
from default.metadata import META_ALIASES
from default.services import SERVICES
from default.site_settings import SITE_SETTINGS
from default.storages import STORAGES
from default.views import VIEWS


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

template = config["site_name"]

if template and os.path.exists("template_{}".format(template)):
    print "Using template", template
    try:
        ACTIONS = __import__('template_{}.actions'.format(template), globals(), locals(), ['ACTIONS'], -1).ACTIONS
    except ImportError:
        print ("Using default settings for actions")
    try:
        CHANNELS = __import__('template_{}.channels'.format(template), globals(), locals(), ['CHANNELS'], -1).CHANNELS
    except ImportError:
        print ("Using default settings for channels")
    try:
        FOLDERS = __import__('template_{}.folders'.format(template), globals(), locals(), ['FOLDERS'], -1).FOLDERS
    except ImportError:
        print ("Using default settings for folders")
    try:
        BASE_META_SET = __import__('template_{}.metadata'.format(template), globals(), locals(), ['BASE_META_SET'], -1).BASE_META_SET
    except ImportError:
        print ("Using default settings for metadata")
    try:
        META_ALIASES = __import__('template_{}.metadata'.format(template), globals(), locals(), ['META_ALIASES'], -1).META_ALIASES
    except ImportError:
        print ("Using default settings for metadata")
    try:
        SERVICES = __import__('template_{}.services'.format(template), globals(), locals(), ['SERVICES'], -1).SERVICES
    except ImportError:
        print ("Using default settings for services")
    try:
        SITE_SETTINGS = __import__('template_{}.site_settings'.format(template), globals(), locals(), ['SITE_SETTINGS'], -1).SITE_SETTINGS
    except ImportError:
        print ("Using default settings for site_settings")
    try:
        STORAGES = __import__('template_{}.storages'.format(template), globals(), locals(), ['STORAGES'], -1).STORAGES
    except ImportError:
        print ("Using default settings for storages")
    try:
        VIEWS = __import__('template_{}.views'.format(template), globals(), locals(), ['VIEWS'], -1).VIEWS
    except ImportError:
        print ("Using default settings for views")
    try:
        VIEWS = __import__('template_{}.users'.format(template), globals(), locals(), ['USERS'], -1).USERS
    except ImportError:
        print ("Using default settings for users")

    try:
        CS = __import__('template_{}.cs'.format(template), globals(), locals(), ['CS'], -1).CS
    except ImportError:
        CS = {}
        print ("Using default settings for views")


db = DB()

##############################################################  
## create db structure

if options.structure:
    print ("Recreating database structure")
    for q in DB_STRUCTURE:
        db.query(q)
    db.commit()
    
## create db structure
##############################################################
## metadata set

if not options.structure:
    if options.objects:
        print ("Removing objects")
        db.query("TRUNCATE TABLE nx_assets, nx_meta, nx_items, nx_bins, nx_events, nx_jobs RESTART IDENTITY")
        db.commit()



print "Installing metadata structure"
db.query("TRUNCATE TABLE nx_meta_types, nx_meta_aliases RESTART IDENTITY")
for ns, tag, editable, searchable, class_, default, settings in BASE_META_SET:
    q = """INSERT INTO nx_meta_types (namespace, tag, editable, searchable, class, default_value, settings) VALUES ('%s' ,'%s', %d, %d, %d, '%s', '%s')""" % \
           (ns, tag, editable, searchable, class_, default, json.dumps(settings))
    db.query(q)
db.commit()

for tag, lang, alias, col_header in META_ALIASES:
    db.query("""INSERT INTO nx_meta_aliases (tag, lang, alias, col_header) VALUES (%s ,%s, %s, %s)""", [tag, lang, alias, col_header])
db.commit()



db.query("TRUNCATE TABLE nx_settings, nx_folders, nx_services, nx_storages, nx_actions, nx_channels, nx_views, nx_cs RESTART IDENTITY")
db.commit()

print "Installing site settings"
for key, value in SITE_SETTINGS:
    q = """INSERT INTO nx_settings(key,value) VALUES ('%s','%s')""" % (key, value)
    db.query(q)
db.commit()

print "Installing folders"
for id_folder, title, color, meta_set in FOLDERS:
    validator_fname = os.path.join("template_{}".format(template), "validators" , "{}.py".format(id_folder))
    if os.path.exists(validator_fname):
        validator = open(validator_fname).read()
    else:
        validator = None

    db.query("INSERT INTO nx_folders (id_folder, title, color, meta_set, create_script) VALUES (%s,%s,%s, %s, %s)", (id_folder, title, color, json.dumps(meta_set), validator))
db.commit()

print "Installing services"
for agent, title, host, autostart, loop_delay in SERVICES:
    service_settings_fname = os.path.join("template_{}".format(template), "service_settings" , "{}.xml".format(title))
    if os.path.exists(service_settings_fname):
        settings = open(service_settings_fname).read()
    else:
        settings = "<settings></settings>"
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

print "Installing actions"
for id_action, title, config in ACTIONS:
    q = "INSERT INTO nx_actions (id_action, title, config) VALUES (%d,'%s', '%s')" % (id_action, title, db.sanit(config))
    db.query(q)
db.commit()

print "Installing channels"
for id_channel, channel_type, title, config in CHANNELS:
    q = "INSERT INTO nx_channels (id_channel, channel_type, title, config) VALUES (%d, %d, '%s', '%s')" % (id_channel, channel_type, title, db.sanit(json.dumps(config)))
    db.query(q)
db.commit()

print "Installing views"
for title, config in VIEWS:
    db.query("INSERT INTO nx_views (owner, title, config) VALUES (0, %s, %s)", [title, config])
db.commit()

print "Installing CS"
for cs in CS:
    for v, t in CS[cs]:
        db.query("INSERT INTO nx_cs (cs, value, label) VALUES (%s, %s, %s)", [cs, v, t]) 
db.commit()