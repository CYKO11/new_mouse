import socket
import time

class socketClient:
    def __init__(self, ip, port):
        connection = socket.socket()
        connection.connect((ip, port))
        self.connection = connection

    def send(self, message):
        self.connection.send(message.encode())

    def closeConn(self):
        self.connection.close()
