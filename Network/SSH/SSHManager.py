import paramiko
from Configurations.cm import Cm

class SSHConnection:

    def __init__(self,userName,password,host):
        self.username=userName
        self.password=password
        self.host=host
        self.nbytes = int(Cm('config.ini').config["SSH"]["maxSize"])
        self.port=22

    def TransferFile(self,source,destenation):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.host, username=self.username, password=self.password)

        sftp = ssh.open_sftp()
        sftp.get(source, destenation)
        ssh.close()

    def SendCommand(self,command):
        client = paramiko.Transport(self.host,self.port)
        paramiko.SSHConfig()
        client.connect(username=self.username, password=self.password)
        stdout_data = []
        stderr_data = []
        session = client.open_channel(kind='session')
        session.exec_command(command)
        while True:
            if session.recv_ready():
                stdout_data.append(session.recv(self.nbytes))
                print (stdout_data)
            if session.recv_stderr_ready():
                stderr_data.append(session.recv_stderr(self.nbytes))
            if session.exit_status_ready():
                break

        session.close()
        client.close()
        return stdout_data