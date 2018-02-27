# Sprint2: deploy.py Code
# Danai Avgerinou, Ting Ting Liu, Shannon McNish, Jose A. Rodilla, Kerem Turgutlu
# Group Name: Bowbowbowbowsquaddd

import paramiko
import time


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
    
    # change testtest from ec2-user
    ssh.connect(hostname, username='testtest', key_filename=private_key)
    if ssh == False:
        print 'Connection Error'
    else:
        print 'Successful Connection'

    # Clone the repo and start flask app
    ssh.exec_command('rm -rf sprint/; git clone https://github.com/KeremTurgutlu/sprint')
    time.sleep(2)
    ssh.exec_command("""screen -d -m -s "runflask" python ~/sprint/flask_server.py %s"""%prefix)  
    ssh.close()


# Please append deploy('path_to_ssh_key_private_key', 'server-address', 'prefix') below:
