'''
from server2 import FileHandler
from ftp import FtpClient

fileHandler = FileHandler()
ftpClient = FtpClient('192.168.1.104', 3000)


blocks = fileHandler.readBinaryBlockArray("F:/rota1.png")
ftpClient.upload(blocks, 'rota1.png')

print('Arquivo enviado!')
'''
import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.104', 3000))
print('Pós connect')
        
# Envia o nome do arquivo a ser criado no servidor
client.send('filename'.encode())


