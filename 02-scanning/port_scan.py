import socket
import termcolor

def scan(target, ports):
    for port in range(ports):
        scan_port(target, port)


def scan_port(target: str, port: int):
    try:
        socket_object = socket.socket()
        socket_object.connect((target, port))

        print(f'[+] - Port Open: { port }')
        socket_object.close()
    except:
        pass



if __name__ == '__main__':
    targets: str = input('[*] - Enter target to scan(split them by comma): ')
    ports: str = int(input('[*] - Enter how many ports you want to scan: '))

    if ',' in targets:
        print('[*] - Scanning multiple targets')
        for ip_address in targets.split(','):
            scan(ip_address.strip(' '), ports)
    else:
        scan(targets, ports)
