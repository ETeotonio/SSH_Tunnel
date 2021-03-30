from sshtunnel import SSHTunnelForwarder
class ssh_tunnel:
    def __init__(self,src_ip, src_port,dest_ip, dest_port,username,password):
        self.src_ip=src_ip
        self.src_port = src_port
        self.dest_ip = dest_ip
        self.dest_port = dest_port
        self.username = username
        self.password = password

    def validate_values(self, ip, port):
        valid = False
        if(len(ip)>0):
            for (octet in ip.split('.')):
                if(octet >= 0 && octet <=255):
                    print("Octet %s is valid",octet)
                    valid=True
                else:
                    print("Octet %s is not valid",octet)
                    valid=False
                    break
        if(port>0 && port <65550 ):
            valid=True
        else:
            valid=False
        return valid
    
    def start_tunnel (self):
        if(validate_values(self.src_ip,self.src_port) && validate_values(self.dest_ip,self.dest_port)):
            try:
                ssh_server = SSHTunnelForwarder(self.src_ip,ssh_username=self.username,ssh_password=self.password,remote_bind_access=(self.dest_ip,self.dest_port))
                ssh_server.Start()
                print(ssh_server.local_bind_port)
            except:
                print("Error Establishing connection to %s",self.src_ip)

