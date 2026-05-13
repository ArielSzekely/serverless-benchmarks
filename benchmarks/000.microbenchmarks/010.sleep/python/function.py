# Copyright 2020-2025 ETH Zurich and the SeBS authors. All rights reserved.

from time import sleep

from . import storage

def handler(event):

    storage.storage.get_instance()._clnt.log_spawn_latency("Paper.Initialization.None", 0)
    sleep_time = event.get('sleep')
    sleep(sleep_time)
    return { 'result': sleep_time }
