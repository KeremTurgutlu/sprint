'''
pip install paramiko
'''

import paramiko
from user_definition import *

#Connect to server
print "Connecting to box"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username = username, key_filename = key_filename)

if ssh == False:
    print 'Connection Error'
else: print 'Successful Connection'

#Clone git repo to server

"""
git already installed in server


"""

ssh.exec_command('git clone https://github.com/KeremTurgutlu/sprint')




