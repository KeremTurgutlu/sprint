# Sprint1: process.py Code
# Danai Avgerinou, Ting Ting Liu, Shannon McNish, Jose A. Rodilla, Kerem Turgutlu
# Group Name: Bowbowbowbowsquaddd

import json
import os
import sys
import time
import logging
from logging.handlers import TimedRotatingFileHandler

# definitions
prefix = sys.argv[1]
check_dir = '/srv/runme/'
path = check_dir + prefix

def rotate_files(path):
    """
    Creates a rotating log
    """
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    #add a roating handler
    handler = TimedRotatingFileHandler(path, when="m", interval=2)

    logger.addHandler(handler)
 
    for i in range(6):
        logger.info("This is a test!")
        time.sleep(75)


def process_json(check_dir, prefix):

    #get files under check_dir directory
    files = os.listdir(check_dir)

    #check files that begin with prefix
    n = len(prefix)
    good_files = [f for f in files if f[:n] == prefix]
    name_age = ''

    #open every file
    for file in good_files:
        # print 'reading {}...\n'.format(check_dir + file)
        with open(check_dir + file) as f:
            for line in f:
                try:
                    d = json.loads(line)
                    name = d['name']
                    age = d['prop']['age']
                    name_age += name + '\t' + str(age) + '\n'
                except:continue

    #output: proc.txt
    with open(check_dir + prefix + '/proc.txt', 'w+') as f:
        f.write(name_age)

def put_json_in_raw(check_dir, prefix):
    #get files under check_dir directory
    files = os.listdir(check_dir)

    #check files that begin with prefix
    n = len(prefix)
    good_files = [f for f in files if f[:n] == prefix]
    name_age = ''

    #open every file
    for file in good_files:
        with open(check_dir + file) as f:
            for line in f:
                try:
                    d = json.loads(line)
                except: continue
    #output: Raw.txt
    with open(check_dir + prefix + '/Raw.txt', 'w+') as f:
        f.write(d)




