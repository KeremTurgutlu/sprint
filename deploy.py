'''
pip install paramiko
'''

import paramiko
from user_definition import *

def deploy(key_filename, hostname, prefix):
    #Connect to server
    print "Connecting to box"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username = 'ec2-user', key_filename = key_filename)

    if ssh == False:
        print 'Connection Error'
    else: print 'Successful Connection'

    #Clone git repo to server

    """
    git, crontab  already installed in server
    """
    # clone repo to home dir
    ssh.exec_command('git clone https://github.com/KeremTurgutlu/sprint')
    # run process.py with crontab every 5 minutes
    ssh.exec_command('crontab -l > mycron')
    ssh.exec_command('echo "* * * * * python ~/sprint/process.py {}" >> mycron'.format(prefix))
    ssh.exec_command('crontab mycron')

#deploy.py
hostname = '54.200.19.10'
key_filename = '/home/kerem/.ssh/bowbow.pem'
prefix = 'blob'

deploy(key_filename, hostname, prefix)

