#!python
from struct import *
from framework import parser
import socket
import pcapy
import sys
import logging

# Called when running directly to begin sniffing
def main(argv):
    #list all devices
    devices = pcapy.findalldevs()
    
    #ask user to enter device name to sniff
    #print "Available devices are:"
    for d in devices:
        print (d)
    print ("")
    
    #dev = raw_input("Enter device name to sniff : ")
    #print "Sniffing device " + dev
    
    cap = pcapy.open_live('\\Device\\NPF_{198D3DE6-6DFD-42A2-ADB4-9BCD50A57982}' , 65536 , 1 , 100000)
    
    #start sniffing packets
    while(1):
        (header, packet) = cap.next()
        #print ('%s: captured %d bytes, truncated to %d bytes' %(datetime.datetime.now(), header.getlen(), header.getcaplen()))
        parse_packet(packet)

# function to parse a packet
def parse_packet(packet):
    logging.basicConfig(filename='packets.log',level=logging.DEBUG)
    
    if not packet:
        return
    
    #parse ethernet header
    eth_length = 14
    
    eth_header = packet[:eth_length]
    try:
        eth = unpack('!6s6sH' , eth_header)
    except:
        return
    eth_protocol = socket.ntohs(eth[2])

    #Parse IP packets, IP Protocol number = 8
    if eth_protocol == 8:
        #Parse IP header
        #take first 20 characters for the ip header
        ip_header = packet[eth_length:20+eth_length]
        
        #now unpack them :)
        iph = unpack('!BBHHHBBH4s4s' , ip_header)

        version_ihl = iph[0]
        ihl = version_ihl & 0xF

        iph_length = ihl * 4

        protocol = iph[6]

        #Parse TCP protocol, protocol #6
        if protocol == 6:
            t = iph_length + eth_length
            tcp_header = packet[t:t+20]

            #now unpack them :)
            tcph = unpack('!HHLLBBHHH' , tcp_header)
            
            source_port = tcph[0]
            dest_port = tcph[1]
            doff_reserved = tcph[4]
            tcph_length = doff_reserved >> 4
            
            h_size = eth_length + iph_length + tcph_length * 4
            data_size = len(packet) - h_size
            
            #get data from the packet
            data = packet[h_size:]
            
            if source_port == 3600 or dest_port == 3600:
                #Don't show me blank packets.
                if data and bytearray(data) is not 0:
                    if source_port == 3600:
                        print ("Server:")
                    else:
                        print ("Client:")
                    parser.parse_data(data)
                    try:
                        logging.getLogger().debug(data)
                    except:
                        print ("logging error")

# If ran directly, begin the sniffer
if __name__ == "__main__":
    main(sys.argv)