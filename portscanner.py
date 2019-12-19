import threading
import socket
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import queue


# port_range = range(10000)
file = 'ports_list.txt'
open_ports = []


def read_ports_from_file():
    '''
    Reading comma separated values from file and return port list
    '''
    ports = []    
    with open(file, "r") as filestream:
        for line in filestream:
            ports_line = line.replace('\n', '').replace(' ', '').split(",")
            for port in ports_line:
                if port != '':
                    ports.append(int(port))
    return ports 


def portscan(port, target):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        connection = s.connect((target, port))
        print('Port :', port, "is open.")
        open_ports.append(port)
        connection.close()  
    except:
        pass


def do_scan(ports, target):
    print('Scanning host: ', target)
    print('-' * 35)
    threads = []  
    open_ports = [] # Reset

    # Готовим потоки
    for port in ports:  
        threads.append(threading.Thread(target=portscan, args=(port, target,)))

    # Запускаем каждый поток
    for thread in threads:
        thread.start()

    # Ждем завершения каждого потока
    for thread in threads:
        thread.join()



def scan(ports, target):
     do_scan(ports, target)
     return open_ports

