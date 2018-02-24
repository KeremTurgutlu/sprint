import paramiko
from flask_server import *

def deploy(private_key, hostname, prefix):
    """
    Inputs:
        private_key(str) : path for key file
        server_address(str) : address of server
        prefix (str) : prefix to look for while processing
    """
    # Connect to server
    print "Connecting to Box"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username='testtest', key_filename=private_key)
    if ssh == False:
        print 'Connection Error'
    else:
        print 'Successful Connection'

    # Clone the repo and start flask app
    ssh.exec_command('rm -rf sprint/; git clone https://github.com/KeremTurgutlu/sprint')
    ssh.exec_command('python ~/sprint/flask_server.py '.format(prefix))
    ssh.close()

    pass