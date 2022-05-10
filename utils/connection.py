import paramiko

# Test conection and return boolean
def test(ip):
    user = "user"
    password = "password"
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,user,password,timeout=5)
        print('%s\tOK'%(ip))
        return True
    except:
        print('%s\tKO'%(ip))
        return False

# Add ssh public key
# You require id_rsa.pub in the project folder
# Change de content of cmd variable
def add_ssh_key(ip):
    user = "user"
    password = "password"

    # Example of using the cmd, with different variables
    # hola = "hola"
    # adios = "adios"
    # cmd = '''
    # echo hola
    # echo {}
    # echo adios
    # echo {}
    # '''.format(hola,adios)

    # Incorporate the id_rsa.pub in the authorized_keys dir
    with open ("id_rsa.pub", "r") as myfile:
        data = myfile.read().strip()
    cmd = '''
    mkdir -p /home/ahernandez/.ssh;touch /home/ahernandez/.ssh/authorized_keys
    echo {} > /home/ahernandez/.ssh/authorized_keys
    chown -R ahernandez:admindob /home/ahernandez
    chmod 700 /home/ahernandez/.ssh
    '''.format(data)

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,user,password,timeout=5)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        # print(stderr.read())
        ssh.close()
    except :
        print('%s\tKO'%(ip))


# Connect with ssh key
# Sometimes fails because paramiko bug: 
# https://stackoverflow.com/questions/70565357/paramiko-authentication-fails-with-agreed-upon-rsa-sha2-512-pubkey-algorithm
# https://github.com/paramiko/paramiko/issues/1961
def ssh_key(ip):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=22, username = "ahernandez", key_filename='id_rsa', timeout=5)

        # To solve de bug
        # ssh.connect(hostname=ip, port=22, username = "ahernandez", key_filename='id_rsa', timeout=5, disabled_algorithms=dict(pubkeys=["rsa-sha2-512", "rsa-sha2-256"]))
        
        # stdin,stdout,stderr = ssh.exec_command("date")
        # print(stderr.read())
        print('%s\tOK'%(ip))
        ssh.close()
    except :
        print('%s\tKO'%(ip))
