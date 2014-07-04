import psycopg2
import socket
import json
import os
import sys

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

class DB():
    def __init__(self):
        self._connect()

    def _connect(self):  
        self.conn = psycopg2.connect(database = config['db_name'], 
                                     host     = config['db_host'], 
                                     user     = config['db_user'],
                                     password = config['db_pass']
                                     ) 
        self.cur = self.conn.cursor()

    def query(self,q,*args):
        self.cur.execute(q,*args)

    def sanit(self, instr):
        #TODO: THIS SHOULD BE HEEEEAAAVILY MODIFIED
        try: return str(instr).replace("''","'").replace("'","''").decode("utf-8")
        except: return instr.replace("''","'").replace("'","''")

    def fetchall(self):
        return self.cur.fetchall()
   
    def lastid (self):
        self.query("select lastval()")
        return self.fetchall()[0][0]

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()