class Funcionario(object):
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    
    def calcula_reajuste(self):
        if self.cargo.lower() == 'operador':
            return self.salario * (1.2)
        elif self.cargo.lower() == 'programador':
            return self.salario * (1.18)
        else:
            return self.salario


    def toString(self):
        retorno = self.nome + ' recebe ' + str(self.calcula_reajuste())
        return retorno

import socket

# Declara as constantes de conexao
HOST = ''
PORT = 3000

# Cria um canal para comunicação via socket
chanel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Libera a porta quando o servidor for finalizado com CTRL+C
chanel.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Associar o chanel a um host e porta
chanel.bind((HOST, PORT))

# Define um limite de conexões no chanel
chanel.listen(3)

# Define um limite máximo para conexoes
MAX_CONN = 5
countConn = 0

# Entra em loop para receber várias conexões

conn, client = chanel.accept()
print('O cliente ' + str(client) + ' estabeleceu conexão')   

content = conn.recv(1024)
import pickle
funcionario = pickle.loads(content)
print(funcionario.toString())

    