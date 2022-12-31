**Nmap Scan Types**
add -fN <file_name> to save the output

--
- Nmap is a network mapping and network scanner that allow us to discover hosts and services in a a computer network sending packages and analyzing responses
- `man nmap` to open nmap manual in a terminal

+ `nmap -sS <ip_address>`
    - TCP SYN scan, probably the most popular scan in nmap, the SYN scan really never open a TCP connection
+ `nmap -sT <ip_address>`
    - TCP connect scan, this stablished full connection, require more tiem and is esasily detected, is better the previos one
+ `nmap -sU <ip_address>`
    - UDP connect scan, this is very unpopular due to many services on the internet run over TCP, UDP is much slower and difficult


**Scan Operative System**
--
- `nmap -O <ip_address>`

**Version of service running in a port**
--
+ `nmp -Sv <ip_address>`
    - Deeply scan of the target
    - YOu can add a flag `--version-intensity <0-9>`the default is 7 in the above command
+ `nmap -A <ip_address>`
    - One of the more aggresive scanning options, do not use this in target without permission to scan!

**Filter Ports**
--
If our target is well secured or have a firewall, we must perform the scan as quietly as posible in order to not get detected

+ `nmap -sn <ip_address>, gateway, subnet mask,example 192.168.1.1-255`
    - No port scan -> 
+ `nmap -p <port_range> <ip_address>`
    - filter ports to scan
+ `nmap -F <ip_address`
    -  Scan top 100 ports


**Bypass security measures**
--
We can bypass some security measures such as firewalls or IDS that the target has.
How we know wich ports of a machine are behind a firewall?
+ `nmap -f <ip_address>`
    - This command send tiny fragmented IP Packets, the idea of this is split TCP header over several packets, so itś more complicated for firewalls and IDS to detect what are you doing, it splits the packet in 8 bytes per fragment, if we add other -f, then in 16 bytes and so on.

We can use another option most focused in hiding IP address than bypassing security, and that is creating decoys using -D
+ `nmap -D RND:ips_desireds(example 5) <ip_address>`
    - this scan show to the trget that is not only scanned by you but also by the decoys,so the IDS might report multiple IP address scan them, including ours, but it will not be able to determine wich one is real, it generate random ip adress
+ `nmap -D ip1,ip2,ip3,ME <ip_address>`
    - This is useful for scan in local network yo can specific the ips, and the ME key to include our ip address

+ `nmap -S <fake_ip_address> -Pn -e <network interface> -g`
    - Use to spoof our ip address, it will make the target think that someone else is scanning them, the problem is that we will not get results of scan back since they will be sent to the ip address you are trying to impersonate, the -g help us to bypass firewalls



### Firewall
Is a network security system that monitors network traffic and itś based on the security rules that are predeterminated.
There are two firewall types:
- Network firewalls = filter traffic between two or more networks
- Host-based firewalls = only filter that is going in or out from that specific machine

### IDS
Intrusion Detection System, is usually a software application that monitors network for any malicius activity.
Some of the nmap commands above can get caught by a IDS 