# Theory behind scanning
- Second phase of penetration testing
- We are mainly focused in technology side
- We are going to directly exchange packages with our target and when the target send us package back, we are going to discover something about it
- we are going to send TCP and UDP packages to the target
- TCP and UDP ares protocols used for sending bits of data, knonss as packages

## Goal
- We are looking for open ports(virtual open ports that every machine has)
- Every machine has 65535 ports, if any of these areopen and vulnerable, then the target is exploitable

### common default ports
- 80 -> http
- 443 -> https
- 21 -> ftp
- 22 -> ssh
- 25 -> smtp
- 53 -> dns

**Vulnerable Machines**
--
1. Metasploitable
    + `http://downloads.metasploit.com/data/metasploitable/metasploitable-linux-2.0.0.zip`
