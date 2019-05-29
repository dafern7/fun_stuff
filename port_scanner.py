import socket
import sys
import time
#takes a rly long time to process lots of ports-could add threading
#input = [program_name port_start_number port_end_number host_name_1 host_name_2 ... ]

n = len(sys.argv) #num of args
#create a dictionary of key,value pairs for known port names
dict = {}
dict[20] = 'FTP-DATA'
dict[21] = 'FTP'
dict[22] = 'SSH'
dict[23] = 'TELNET'
dict[25] = 'SMTP'
dict[53] = 'DNS'
dict[67] = 'DHCP'
dict[68] = 'DHCP'
dict[69] = 'TFTP'
dict[80] = 'HTTP'
dict[110] = 'POP3'
dict[123] = 'NTP'
dict[143] = 'IMAP'
dict[161] = 'SNMP'
dict[162] = 'SNMP'
dict[179] = 'BGP'
dict[389] = 'LDAP'
dict[443] = 'HTTPS'
dict[546] = 'DHCPv6-client'
dict[547] = 'DHCPv6-server'
dict[636] = 'LDAPS'
dict[990] = 'FTPS'

for hrange in range(3,n): #parse through host numbers (should be args 3 and up)
    host = sys.argv[hrange]
    print ("Host",host,"is currently being scanned")
    try:
        for port in range(int(sys.argv[1]),int(sys.argv[2])+1): #first and second arg should be port range 
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #generate socket link
            socket.setdefaulttimeout(0.0000005) #timeout (never seems to trigger)
            t = time.time()
            x = conn.connect_ex((host, port)) #return 0 if successful
            elapsed = time.time() - t
            if x == 0:
                if port in dict:
                    print (host,port,"OPEN",dict[port])
                else:
                    print(host,port,"OPEN")
    #        elif elapsed > 1.5: #bootleg timeout trigger
    #           if port in dict:
    #                print (host,port,"DROPPED",dict[port])
    #            else:
    #                print(host,port,"DROPPED")
            else:
                if port in dict:
                    print (host,port,"CLOSED",dict[port])
                else:
                    print(host,port,"CLOSED")
    except socket.timeout: #exception for socket timeout
         if port in dict:
            print (host,port,"DROPPED",dict[port])
         else:
            print(host,port,"DROPPED")
