#coding:utf8
import requests
import threading

def run():
    print requests.get('http://127.0.0.1:1234/crawler')

def main():
    t_list = []
    for i in xrange(30):
        t_list.append(threading.Thread(target=run,args=()))
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()

if __name__ == '__main__':
    main()