import paramiko


### DEPLOY2 DOESN'T RUN python sprint/flask_server.py {}'.format(prefix) !!!

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
    ssh.connect(hostname, username='ec2-user', key_filename=private_key)
    if ssh == False:
        print 'Connection Error'
    else:
        print 'Successful Connection'

    # Clone the repo and start flask app
    ssh.exec_command('rm -rf sprint/; git clone https://github.com/KeremTurgutlu/sprint')

    ssh.exec_command('screen -d -m -S flask python ~/sprint/flask_server.py {}'.format(prefix))
    ssh.close()

if __name__ == '__main__':
    deploy('/Users/ds-lorean/Documents/USF_old/501_Computation/AWS/694J.pem', '34.216.9.104', 'cats')
