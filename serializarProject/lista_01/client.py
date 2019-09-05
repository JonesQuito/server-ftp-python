# Importando bibliotecas necessárias
import pickle
import socket

from models.funcionario import Funcionario


class ClienteSocket(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def enviar(self, dados):
        try:
            self.client.send(dados)
            return 0
        except Exception as e:
            return e

    def recebe(self):
        return self.client.recv(1024)





f = Funcionario('Jones', 'programador', 2500)
clientSocket = ClienteSocket('192.168.1.104', 3000)

fs = pickle.dumps(f)
clientSocket.enviar(fs)
print(pickle.loads(clientSocket.recebe()))

#fs = pickle.loads(fs)
#print(fs.toString())

