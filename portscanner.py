import threading
import socket

ports = [21, 22, 23, 25, 38, 43, 80, 109, 110, 115, 118, 119, 143,  # Список портов
         194, 220, 443, 540, 585, 591, 1112, 1433, 1443, 3128, 3197,
         3306, 4000, 4333, 5100, 5432, 6669, 8000, 8080, 9014, 9200, 8500, 8501, 9000]

port_range = range(10000)

open_ports = []


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
    for element in ports:   # Перебор в цикле портов
        t = threading.Thread(target=portscan, kwargs={'port': element, 'target': target})  # Создаём поток
        t.start()   # Запуск потока
    print(open_ports)
    return open_ports