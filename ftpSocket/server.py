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
while countConn < MAX_CONN:
    conn, client = chanel.accept()
    print('O cliente ' + str(client) + ' estabeleceu conexão')
    

    filename = str(conn.recv(1024)).split("'")[1]
    file = open(filename, 'wb')

    print(filename)
   
    while True:
        content = conn.recv(1024)
        if not content:
            break
        file.write(content)
        print(content)
    
    countConn = countConn + 1
    file.close()



print('HOST')