#import ssh_tunnel
import argparse

params_parser = argparse.ArgumentParser(description="Establishes a tunnel via SSH to a remote host")
params_parser.add_argument('--remote_ip',help="Source IP")
params_parser.add_argument('--remote_port',help="Source Port")
params_parser.add_argument('--dest_port',help="Dest Port")
params_parser.add_argument('--username',help="Username")
params_parser.add_argument('--password',help="Password")

args = params_parser.parse_args()

if(args.remote_ip == None):
    params_parser.print_help()

#tunnel = ssh_tunnel.ssh_tunnel(args.remote_ip,args.remote_port,args.dest_port)