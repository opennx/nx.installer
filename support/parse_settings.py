#!/usr/bin/env python
import os
import sys
import json

settings_files = [
    "/etc/nebula.json",
    "local_settings.json"
]

config = {}
for settings_file in settings_files:
    if os.path.exists(settings_file):
        try:
            config.update(json.load(open(settings_file)))
        except:
            pass

try:
    print config[sys.argv[1]]
except:
    sys.exit(1)
