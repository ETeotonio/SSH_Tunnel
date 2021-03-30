import paramiko

class ssh_tunnel:
    def __init__(self,src_ip, src_port,dest_ip, dest_port):
        self.src_ip=src_ip
        self.src_port = src_port
        self.dest_ip = dest_ip
        self.dest_port = dest_port

    def validate_values(self, ip, port):
        valid = False
        if(len(ip)>0):
            for (octet in ip.split('.')):
                if(octet >= 0 && octet <=255):
                    print("Octet %s is valid",octet)
                else:
                    print("Octet %s is not valid",octet)
                    break
        return valid
    
    def start_tunnel (self, src_ip,src_port,dest_ip,dest_port:
        
