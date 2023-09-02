#!/bin/python3
#creator--Patxa

import subprocess, re, sys

def argumentos():
    print( "\n['!']""Use: Python3" + "<IP-adress>\n")
    sys.exit(1)
def getTtl(ip_address):
    p=subprocess.Popen(["ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
    (out, err) = p.communicate()
    out = out.split()
    out = out[12].decode('utf-8')
    ttl = re.findall(r"\d{1,3}", out)[0]
    
    return ttl
if __name__ == '__main__':
    try:
        ip_address = sys.argv[1]
        ttl_value = getTtl(ip_address)
        ttl_value = int(ttl_value)
        
        if ttl_value >= 0 and ttl_value <= 64:
            print("\n Target's OS is -> Linux \n")
        elif ttl_value >= 65 and ttl_value <= 128:
            print("\n Target's OS is -> Windows \n")
        else:
            print("\n Target's OS is -> Solaris/AIX \n")
    except:
        argumentos()