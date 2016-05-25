import socket
HOSTNAME = socket.gethostname()

## agent, title, host, autostart, loop_delay, settings

SERVICES = [
    ("hive",        "Hive",      HOSTNAME, 1, 5),
    ("meta",        "Meta",      HOSTNAME, 1, 5),
    ("broker",      "Broker",    HOSTNAME, 1, 10),
    ("conv",        "Conv",      HOSTNAME, 1, 10),
    ("play",        "Play",      HOSTNAME, 1, 5),
    ("messaging" ,  "Messaging", HOSTNAME, 1, 5)
]


