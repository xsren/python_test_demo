#coding:utf8
import time
import functools
import requests
import json
import socket

data = json.dumps({'aaa':'bbb'})
count = 10000

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        t0 = time.time()
        res = func(*args, **kw)
        t_diff = time.time() - t0
        print "%s, use time: %s"%(func.__name__, t_diff)
        return res
    return wrapper

@timer
def send_to_http_server():
    url = 'http://127.0.0.1:8081/test'
    for i in xrange(count):
        requests.post(url, data=data)

@timer
def send_to_socket_server():
    # 创建一个socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1', 8080))
    for i in xrange(count):
        s.send(data)
        recv(s)
    # 关闭连接:
    s.close()

def recv(s):
    # 接收数据:
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        return d

if __name__ == '__main__':
    send_to_http_server()
    send_to_socket_server()