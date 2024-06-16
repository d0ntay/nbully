import socket

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
