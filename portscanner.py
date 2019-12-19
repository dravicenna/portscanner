import threading
import socket
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import queue

# TODO remove hardcoded portlist
# ports = [21, 22, 23, 25, 38, 43, 80, 109, 110, 115, 118, 119, 143,  # Список портов
#          194, 220, 443, 540, 585, 591, 1112, 1433, 1443, 3128, 3197,
#          3306, 4000, 4333, 5100, 5432, 6669, 8000, 8080, 9014, 9200, 8500, 8501, 9000]

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

