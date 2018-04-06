#!/usr/bin/env python3
''' 
    lanchat.py
    A program that supports scanning and UDP chat
    Scanning is achieved by using the scapy module
    UDP chat is achieved using the socket module for
    sending and receving messages
'''

import sys
import socket
import select
from sys import argv
from scapy.all import *
import builtins

def scan():
    print("===========Lan Scanner===========")
    
    while True:
        try:
            interface = raw_input("Enter network interface: ")
            ip = raw_input("Enter IP: ")
            
            print("Scanning")

            conf.verb = 0
            ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = ip), timeout = 2, iface = interface, inter = 0.1)

            print("MAC Address - IP Address")
            for send, recv in ans:
                print(recv.sprintf(r"%Ether.src% - %ARP.psrc%"))
            print("Scan ended")

        except KeyboardInterrupt:
            print("Scanner shutdown by user")
            break

    print("Scan complete")

def send():
    print("==========UDP Chat Sender==========")
    
    host = raw_input("Enter IP: ")
    print("Enter space to set default port 1027" )
    user_port = raw_input("Connect to Port Number: ")
    if user_port == "":
        port = int("1027", 16)
    else:
        port = int(user_port, 16)

    send_address = (host, port)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(False)
    sock.bind(('', port))

    print("Press 'ctrl + c' to exit")
    print("Connecting to port", hex(port))
    print("Type your message")

    while True:
        try:
            message, address = sock.recvfrom(5000)
            message = message.strip("\n")
            if message:
                print(address, "->", message)
        except:
            pass
        
        message = getLine();
        if message != False:
            sock.sendto(message, send_Address)

def main():
    if len(sys.argv) < 2:
        print("Usage: python lanchat.py [--scan] [--send]")
        return
    if sys.argv[1] == "-h":
        print("Usage: python lanchat.py [--scan] [--send]")
        
    if sys.argv[1] == "--scan":
        scan()
    
    if sys.argv[1] == "--send":
        send()

if __name__ == '__main__':
    main()
