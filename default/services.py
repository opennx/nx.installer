import socket
HOSTNAME = socket.gethostname()

## agent, title, host, autostart, loop_delay, settings

SERVICES = [
("hive",   "Hive"  , HOSTNAME, 1, 5 ,"""<settings></settings>"""),
("meta",   "Meta"  , HOSTNAME, 1, 5 ,"""<settings></settings>"""),
("broker", "Broker", HOSTNAME, 1, 10 ,"""<settings></settings>"""),
("conv",   "Conv",   HOSTNAME, 1, 10 ,"""<settings></settings>"""),
("play",   "Play",   HOSTNAME, 1, 5 ,"""<settings></settings>"""),
("messaging" ,"Messaging", HOSTNAME, 1, 5 ,"""<settings></settings>""")
]


