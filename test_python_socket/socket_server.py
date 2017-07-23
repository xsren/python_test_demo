#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, threading
import struct


def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    while True:
        data = recv_msg(sock)
        print data
        if data is None:
            break
            # send_msg(sock,'Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def send_msg(sock, msg):
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


def recv_msg(sock):
    # Read message length and unpack it into an integer
    try:
        raw_msglen = recvall(sock, 4)
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
        return recvall(sock, msglen)
    except Exception as e:
        print str(e)
        return None


def recvall(sock, n):
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


# 监听端口:
s.bind(('0.0.0.0', 9999))
s.listen(5)
print 'Waiting for connection...'
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
