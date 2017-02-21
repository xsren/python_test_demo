#coding:utf8

import bsddb3
import time
import random
import hashlib

test_num = 10000000

def md5(s):
    return hashlib.md5(s).hexdigest()

def insert(db):
    t0 = time.time()
    for i in xrange(test_num):
        db[str(i)] = None
    print time.time() - t0

def insert_md5(db):
    t0 = time.time()
    for i in xrange(test_num):
        db[md5(str(i))] = None
    print time.time() - t0

def query(db):
    i = random.randint(0,test_num)
    t0 = time.time()
    print db.has_key(str(i))
    print time.time() - t0

def query_md5(db):
    i = random.randint(0,test_num)
    t0 = time.time()
    print db.has_key(md5(str(i)))
    print time.time() - t0

def main():
    db1 = bsddb3.hashopen('test1.db', 'c')
    #插入1000w整数
    insert(db1)
    query(db1)
    #插入1000w整数得到的md5
    db2 = bsddb3.hashopen('test2.db', 'c')
    insert_md5(db2)
    query_md5(db2)


if __name__ == '__main__':
    main()