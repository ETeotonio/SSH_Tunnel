from sshtunnel import SSHTunnelForwarder
class ssh_tunnel:
    def __init__(self,src_ip, src_port, dest_port,username,password):
        self.src_ip=src_ip
        self.src_port = src_port
        self.dest_port = dest_port
        self.username = username
        self.password = password

    def validate_values(self, ip, port):
        valid = False
        if(len(ip)>0):
            for octet in ip.split('.'):
                if(octet >= 0 and octet <=255):
                    print("Octet %s is valid",octet)
                    valid=True
                else:
                    print("Octet %s is not valid",octet)
                    valid=False
                    break
        if(port>0 and port <65550 ):
            valid=True
        else:
            valid=False
        return valid
    
    def start_tunnel (self):
        if(validate_values(self.src_ip,self.src_port) and validate_values(self.dest_ip,self.dest_port)):
            try:
                ssh_server = SSHTunnelForwarder(self.src_ip,ssh_username=self.username,ssh_password=self.password,remote_bind_access=(self.dest_ip,self.dest_port))
                ssh_server.Start()
                print(ssh_server.local_bind_port)
                return ssh_server
            except:
                print("Error Establishing connection to %s",self.src_ip)

    def stop_tunnel (self, ssh_server):
        print("Stopping tunnel ")
        ssh_server.Stop()

    