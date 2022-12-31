**Scanning Practice**
--
1. Before scan specific machine we must first discover what machine we got on our network(how manyhosts are activated and what are their ips)
    + `arp -a`
    + `netdiscover`
        - Best option

2. nmap, this is a very useful tool to perform pentesting, it is a network mapper, free and open source, nmap by default scan the 1000 most known ports,not the 65000
    + `nmap <ip_address>`
        - Basic scan



**Tips**
--
1. `netstat -nr` => get router ip
