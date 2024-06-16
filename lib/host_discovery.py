import nmap

def host_discovery(network):
    nm = nmap.PortScanner()
    print('[*] Scanning network for active hosts...')
    nm.scan(hosts=network, arguments='-sn')
    for i,host in enumerate(nm.all_hosts()):
        print(f'[{i}] {host}')
    print('Scan Complete!')
    return nm.all_hosts()
