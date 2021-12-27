import socket
import multiprocessing
from multiprocessing import Process
import requests

send_socket = socket.socket()
receive_socket = socket.socket()
sName = None
cName = "!NAME!Python Client"
global_end = False


def connect(host='127.0.0.1', port=8888):
    send_socket.connect((host, port))
    receive_socket.connect((host, port))
    sName = receive_socket.recv(256)
    sName = bytes.decode(sName, 'utf-8')
    send_socket.send(bytes(cName, 'utf-8'))


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def init_client():
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        p1 = Process(target = receive_data)
        p2 = Process(target = send_data)
        p1.start()
        p2.start()


def receive_data():
    loop = True
    while loop and not global_end:
        message = receive_socket.recv(256)
        if message == "Shut up.":
            loop = False
            global_end = True
        print(f'{sName}:', bytes.decode(message, 'utf-8'))


def send_data():
    loop = True
    while loop and not global_end:
        msg = input()
        msg = bytes(msg, "utf-8")
        send_socket.send(msg)


def main():
    connect()
    init_client()
    send_socket.close()
    receive_socket.close()


if __name__ == '__main__':
    main()
