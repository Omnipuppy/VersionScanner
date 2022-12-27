#!/usr/bin/python
from socket import *

def retBanner(ip,port):
    try:
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return
def main():
    ip = input('(*) Please Enter Target IP Address: ')
    for x in range(1,1001):
        port = x
        portly = str(port)
        banner = retBanner(ip,port)
        if(banner != ''):
            print('(*) For Port %d ' % port)
            print('(*) Host returned service %s' % banner)
        else:
            print('(*) For Port %s , Banner Unavailable' % portly)
main()
