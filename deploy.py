import paramiko
import time

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
    # ssh.exec_command('rm -rf sprint/; rm -r runflask; crontab -r; git clone https://github.com/KeremTurgutlu/sprint')
    # ssh.exec_command('nohup python ~/sprint/flask_server.py %s </dev/null &>/dev/null &' % prefix)
    # ssh.exec_command('screen -S runflask')
    # ssh.exec_command('screen -S runflask -X python ~/sprint/flask_server.py %s' % prefix)
    time.sleep(2)
    # ssh.exec_command('screen -d -m python ~/sprint/flask_server.py %s' % prefix)
    # transport = ssh.get_transport()
    # channel = transport.open_session()
    # channel.exec_command('python ~/sprint/flask_server.py %s' % prefix)
    # time.sleep(2)

    # run process.py with crontab every 5 minutes
    # ssh.exec_command('crontab -e runflask')
    # ssh.exec_command('echo "* * * * * python ~/sprint/flask_server.py {}" >> runflask'.format(prefix))
    # ssh.exec_command('crontab runflask')

    ssh.exec_command("""screen -d -m -s "runflask" python ~/sprint/flask_server.py %s"""%prefix)
    
    ssh.close()

if __name__ == '__main__':
    deploy('/Users/ting2liu/Desktop/pems/t2liu-rec.pem', '54.201.90.219', 'cats')

