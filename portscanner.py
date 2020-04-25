import socket


ip=input('Enter a IP for scan: ')
port_list=[]
for port in range(1,5000):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result=s.connect_ex((ip,port))
    if result==0:
        port_list.append(port)
        print(f'{ip} : {port}        open',f'    open ports: {port_list}')
        print('-'*80)

    else:
        print(f'{ip} : {port}        close',f'    open ports: {port_list}')
        print('-' * 80)

        s.close()