import socket


class FtpClient(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def upload(self, arrayBlock, filename):
        # Cria um objeto de conexão com ipv4 e protocolo tcp
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Estabelece a comunicação com o servidor
        client.connect((self.host, self.port))

        # Envia o nome do arquivo a ser criado no servidor
        client.send(filename.encode())

        for block in arrayBlock:
            client.send(block)

        client.close()

    def download(self):
        pass

    def rename(self):
        pass

    def delete(self):
        pass




class FtpServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.MAX_CONN = 5
        self.countConn = 0




    def send(self):
        pass




    def receive(self):
        # Cria um canal para comunicação via socket
        chanel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Libera a porta quando o servidor for finalizado com CTRL+C
        chanel.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Associar o chanel a um host e porta
        chanel.bind((self.host, self.port))

        # Define um limite de conexões no chanel
        chanel.listen(3)

        print("Aguardando conexão em: ", self.host, ' - ', self.port)

        while self.countConn < self.MAX_CONN:
            conn, client = chanel.accept()
            print('O cliente ' + str(client) + ' estabeleceu conexão')
            filename = str(conn.recv(1024)).split("'")[1]
            file = open(filename, 'wb')

            while True:
                content = conn.recv(1024)
                if not content:
                    break
                file.write(content)

            self.countConn = self.countConn + 1
            file.close()
            conn.close()
            chanel.close()





    def rename(self):
        pass


    def delete(self):
        pass
