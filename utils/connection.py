import paramiko

def ssh(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        print('%s OK\n'%(ip))
        ssh.close()
    except :
        print('%s KO\n' %(ip))