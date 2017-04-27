#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_msg(msg):
    msg1 = struct.pack('>I', len(msg)) + msg
    try:
        mysend(msg1)
    except Exception as e:
        print str(e)

    
def mysend(msg):
    totalsent = 0
    MSGLEN = len(msg)
    one_time_send = 1024
    while totalsent < MSGLEN:
        if len(msg) > one_time_send:
            sent = sock.send(msg[:one_time_send])
            msg = msg[one_time_send:]
        else:
            sent = sock.send(msg)
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent

def recv_msg():
    # Read message length and unpack it into an integer
    try:
        raw_msglen = recvall(4)
    except socket.timeout:
        print 'recv msg timeout ......'
        return None
    except Exception as e:
        print str(e)
        return None

    
    if not raw_msglen:
        print "not raw_msglen"
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    try:
        return recvall(msglen)
    except Exception as e:
        print str(e)
        return None

def recvall(n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = ''
    while len(data) < n:
        if n - len(data) > 4:
            packet = sock.recv(4)
        else:
            packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data


sock.connect(('120.77.54.165', 9999))

for data in ['Michael'*1000, 'Tracy'*1000, 'Sarah'*1000]:
    send_msg(data)
    # print recv_msg()
sock.close()
