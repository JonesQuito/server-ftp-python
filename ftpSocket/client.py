# importa o modulo de socket
import socket

# Dados de conexao ao servidor
HOST = '192.168.1.104'
PORT = 3000

# Cria um objeto de conexão com ipv4 e protocolo tcp
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Estabelece a comunicação com o servidor
client.connect((HOST, PORT))

# Lê um arquivo em modo binario
from server2 import FileHandler
fileHandler = FileHandler()
client.send('arquivoteste.txt'.encode())
buff = fileHandler.readBinaryBlockArray('arquivoteste.txt')


for b in buff:
    client.send(b)


client.close()
#f.close()

print('Arquivo enviado')