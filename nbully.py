import nmap
import socket

def main():
    print("Enter Ip address followed by subnet mask in cidr format")
    network = input('> ')
    hosts = host_discovery(network)
    for i,host in enumerate(hosts):
        print(f'[{i}] {host}')
    print('Scan Complete!')
    print('Select a target')
    target = hosts[int(input('> '))]
    print(f'Target selected : {target}')
    ports = port_discovery(target)
    for i,port in enumerate(ports):
        print(f'[{i}] {port}')
    print('Scan Complete!')

def host_discovery(network):
    nm = nmap.PortScanner()
    print('[*] Scanning network for active hosts...')
    nm.scan(hosts=network, arguments='-sn')
    return nm.all_hosts()

def port_discovery(target):
    open_ports = []
    for port in range(1,1024):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((target,port))
            if result == 0:
                open_ports.append(port)
            s.close()
        except:
            pass
    if len(open_ports) <= 0:
        print('No open ports on this target ;C')
    return open_ports


if __name__ == '__main__':
    main()



