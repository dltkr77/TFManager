# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import socket


def check_server(host, port):
    def _ping(host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port)) == 0
        sock.close()
        return result

    return _ping(host, port)