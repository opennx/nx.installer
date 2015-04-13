nx.installer
============

Scripts for initial nx.server database configuration


Files
-----

### local_settings.json

Database connection

### prerequisities.sh

Installs python dependencies. Additionally, you can use `-f` command line option to install ffmpeg as well 
and/or `-n` option to install nginx.

### install.py

By default, this script (re)creates site settings values (meta types, action, services....).
Object data remain untouched

You can use `-s` to create initial database structure or `-o` to truncate existing object data.


template_sitename
-----------------

Create files in this directory to override default settings.