import sys
import subprocess


def ip_reach(ip_list):
    for ip in ip_list:
        ip = ip.rstrip('\n')

        # stdout, stderr=subprocess.DEVNULL will make ping command not to ouput response
        # shell=True for MacOS
        # ping command verifies IP-level connectivity to another TCP/IP computer
        # by sending Internet Control Message Protocol (ICMP) echo Request messages
        ping_reply = subprocess.call('ping %s -c 1' % (ip,),
                                     stdout=subprocess.DEVNULL,
                                     stderr=subprocess.DEVNULL,
                                     shell=True)
        if ping_reply == 0:  # 0 means ping was success
            print('\n* {} is reachable.\n'.format(ip))
            continue
        else:
            print('\n{} not reachable... Check connectivity and try again.'.format(ip))
            sys.exit()
