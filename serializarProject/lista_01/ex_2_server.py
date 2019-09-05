import socket
import pickle
from threading import Thread
import socket
import pickle

class Pessoa(object):
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    
    def is_maior(self):
        if str(self.sexo).lower() == 'f' and self.idade >= 21:
            return True
        elif str(self.sexo).lower() == 'm' and self.idade >= 18:
            return True
        elif str(self.sexo).lower() not in ['f', 'm']:
            return 'Sexo inválido'
        else:
            return False

class Worker(Thread):
    def __init__(self, conn, client):
        Thread.__init__(self)
        self.conn = conn
        self.client = client

    
    def run(self):
        content = self.conn.recv(1024)
        pessoa = pickle.loads(content)

        self.conn.send(pickle.dumps(pessoa.is_maior()))

class ServerSocket(object):
    def __init__(self, host, port, protocolo):
        self.clients = []
        if protocolo.lower() == 'tcp':
            self.chanel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif protocolo.lower() == 'udp':
            self.chanel = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.chanel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.chanel.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.chanel.bind((host, port))
        self.chanel.listen(10)
        # Define um limite máximo para conexoes
        self.MAX_CONN = 20
        self.countConn = 0



    def listener(self):
        while self.countConn < self.MAX_CONN:            
            conn, client = self.chanel.accept()
            self.countConn += 1
            # criar thread para tratar solicitação
            worker = Worker(conn, client)
            worker.start()


serverSocket = ServerSocket('localhost', 3000, 'tcp')
serverSocket.listener()

