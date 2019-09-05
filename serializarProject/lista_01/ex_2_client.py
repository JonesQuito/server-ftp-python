import socket
import pickle

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


pessoa = Pessoa('Leandra', 21, 'm')
pessoa = pickle.dumps(pessoa)

cliente = ClienteSocket('localhost', 3000)
cliente.enviar(pessoa)

resposta = pickle.loads(cliente.recebe())
if resposta:
    print(pickle.loads(pessoa).nome, 'é maior de idade')
else:
    print(pickle.loads(pessoa).nome, 'é menor de idade')