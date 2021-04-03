import socket
import time

class socketServer:
    def __init__(self, port):
        self.serverSocket = socket.socket()
        self.serverSocket.bind((socket.gethostname(), port))
        self.serverSocket.listen(1)
    
    def listenForConnection(self):
        self.clientConnection, address = self.serverSocket.accept()
    
    def readFromConnection(self):
        return self.clientConnection.recv(1024).decode()
    
    def closeConnection():
        self.clientConnection.close()
