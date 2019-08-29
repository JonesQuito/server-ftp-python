# Importa as bibliotecas necessárias
import os
from ftplib import FTP

# Instancia um objeto ftp e estabelece uma conexão
ftp = FTP('')
ftp.connect('localhost', 3001)
ftp.login('Jones Quito', 'jones1987')
#ftp.login()

# Após conectado, me movo para dentro do repositório padrão do servidor
ftp.cwd('/T:\\UFG\\sisdis1\\serverFTP\\repositorio/')

# Faço a listagem dos arquivos no servidor
ftp.retrlines('LIST')


# Verifica se um dado arquivo já existe, caso contrário cria o arquivo
def createFileIfNotExist(filename):
    if not os.path.isfile(filename):
        open(filename, 'w').close()


# Faz o download de um arquivo especificado no parâmetro        
def downfile(filename):
    createFileIfNotExist(filename)
    ftp.retrbinary('RETR ' + filename, open(filename, 'wb').write, 1024)
    ftp.quit()
    
#downfile('One File any.txt')
    
# Função para upload de arquivo
def uploadfile(ip, port, file, user, passwd):
    localfile = open(file, 'rb')
    
    # Cria uma instância do servidor FTP
    conn = FTP('')
    
    # Connecta no servidor
    conn.connect(ip, port)
    
    # Faz login no servidor
    conn.login(user, passwd)
    
    # Muda para o diretório onde deverá ser feito o upload
    conn.cwd('/T:\\UFG\\sisdis1\\serverFTP\\repositorio/')
    
    # Inicia o upload do arquivo
    conn.storbinary('STOR ' + file, localfile, 1024)
    
    # Fecha a conexão e o arquivo local
    conn.quit()
    localfile.close()
    
    print('Envio concluído!')