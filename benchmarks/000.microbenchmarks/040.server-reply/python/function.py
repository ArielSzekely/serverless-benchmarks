# Copyright 2020-2025 ETH Zurich and the SeBS authors. All rights reserved.

import socket
from time import sleep

from . import storage

def handler(event):

    storage.storage.get_instance()._clnt.log_spawn_latency("Paper.Initialization.None", 0)
    addr = (event.get('ip-address'), event.get('port'))
    socket.setdefaulttimeout(20)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr)
    msg = s.recv(1024).decode()
    return {"result": msg}
