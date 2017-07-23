# encoding: utf-8
"""
@author: xsren 
@contact: bestrenxs@gmail.com
@site: xsren.me

@version: 1.0
@license: Apache Licence
@file: test_log.py
@time: 19/07/2017 3:05 PM

"""
import logging
import logging.handlers
import random
import string

import time


def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


def run():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # file
    log_file_name = "/tmp/spider.log"
    fh = logging.handlers.RotatingFileHandler(log_file_name, maxBytes=1024 * 100, backupCount=1)
    formatter = logging.Formatter(
        '%(asctime)s %(funcName)s[line:%(lineno)d] [%(levelname)s]: %(message)s')
    fh.setFormatter(formatter)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    # stdout
    sh = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(funcName)s[line:%(lineno)d] [%(levelname)s]: %(message)s')
    sh.setFormatter(formatter)
    sh.setLevel(logging.DEBUG)
    logger.addHandler(sh)

    while True:
        logger.info(randomword(random.randint(10, 20)))
        time.sleep(5)


if __name__ == '__main__':
    run()
