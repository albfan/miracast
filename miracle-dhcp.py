#!/usr/bin/env python3

import sys
import socket
import os
import subprocess

sock, sockchild = socket.socketpair(socket.AF_UNIX)

IP='192.168.77'
ip_program='/usr/bin/ip'
p = subprocess.Popen(['/usr/local/bin/miracle-dhcp', '--server', '--prefix='+IP, '--ip-binary='+ip_program
                        , '--netdev', sys.argv[1], '--log-level', '8', '--comm-fd', str(sockchild.fileno())]
                     , pass_fds=[sockchild.fileno()])

sockchild.close()

while True:
    r = sock.recv(1024)
    if not r:
        sys.exit(0)
    print(r)
    if p.poll() is not None:
        sys.exit(p.returncode)
