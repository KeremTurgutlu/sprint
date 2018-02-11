# Sprint1: deploy.py Code
# Danai Avgerinou, Ting Ting Liu, Shannon McNish, Jose A. Rodilla, Kerem Turgutlu
# Group Name: Bowbowbowbowsquaddd

'''
pip install paramiko
'''
import paramiko

def deploy(key_filename, hostname, prefix):
    #Connect to server
    print "Connecting to box"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # change username to 'testtest' for submission
    ssh.connect(hostname, username = 'ec2-user', key_filename = key_filename)

    if ssh == False:
        print 'Connection Error'
    else: print 'Successful Connection'

    #Clone git repo to server

    """
    git, crontab  already installed in server
    """
    # clone repo to home dir
    ssh.exec_command('rm -rf sprint/; rm -r mycron; crontab -r; git clone https://github.com/KeremTurgutlu/sprint')
    print 'Pull from github successfully!'

    # run process.py with crontab every 5 minutes
    ssh.exec_command('crontab -e mycron')
    # ssh.exec_command('crontab -e')
    # ssh.exec_command('echo "5 * * * * python ~/sprint/process.py {}" >> mycron'.format(prefix))
    ssh.exec_command('echo "*/5 * * * * python ~/sprint/process.py {}" >> mycron'.format(prefix))

    # ssh.exec_command('5 * * * * python ~/sprint/process.py {}' prefix)

    ssh.exec_command('crontab mycron')
    ssh.close()

#deploy.py arguments will be changed by user
# hostname = '54.200.19.10'
hostname = '34.217.132.21'
# key_filename = '/home/kerem/.ssh/bowbow.pem'
key_filename = '/Users/danaiavg/Downloads/dan-recon.pem'
prefix = 'blob'
deploy(key_filename, hostname, prefix)

