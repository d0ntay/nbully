from lib.host_discovery import host_discovery
from lib.port_discovery import port_discovery
from lib.escalation import escalate
import os
import sys
def main():
    while True:
        clear()
        banner()
        try:
            print("Enter Ip address followed by subnet mask in cidr format")
            network = input('> ')
            hosts = host_discovery(network)
            print('Select a target')
            target = hosts[int(input('> '))]
            print(f'Target selected : {target}')
            ports = port_discovery(target)
            if len(ports) <= 0:
                sys.exit(f'\nGoodbye!')
            target_port = ports[int(input('> '))]
            escalate(target_port)
            break
        except:
            sys.exit(f'\nGoodbye!')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def banner():
    print(r"""
    $$\   $$\       $$$$$$$\  $$\   $$\ $$\       $$\   $$\     $$\ 
    $$$\  $$ |      $$  __$$\ $$ |  $$ |$$ |      $$ |  \$$\   $$  |      
    $$$$\ $$ |      $$ |  $$ |$$ |  $$ |$$ |      $$ |   \$$\ $$  /       
    $$ $$\$$ |      $$$$$$$\ |$$ |  $$ |$$ |      $$ |    \$$$$  /        
    $$ \$$$$ |      $$  __$$\ $$ |  $$ |$$ |      $$ |     \$$  /         
    $$ |\$$$ |      $$ |  $$ |$$ |  $$ |$$ |      $$ |      $$ |          
    $$ | \$$ |      $$$$$$$  |\$$$$$$  |$$$$$$$$\ $$$$$$$$\ $$ |          
    \__|  \__|      \_______/  \______/ \________|\________|\__|

                """)
    print('                             version 1.0')
    print('\n')
if __name__ == '__main__':
    main()



