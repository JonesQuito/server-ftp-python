
class FileHandler(object):
    def __init__(self):
        self.block = []
    def readBinary(self):
        try:
            arquivo = open('imageOriginal.jpg', 'rb')
            arquivo.seek(0,2)
            tamanho = arquivo.tell()
            arquivo.seek(0)

            chuck = 1024
            while arquivo.tell() < tamanho:
                buff = arquivo.read(chuck)
                # nesse ponto deve ter uma conexão de socket aberta para enviar cada bloco lido
                # en contra partida, no outro lado da conexão deve haver um arquivo aberto em modo append ('a+b') para receber
                print(buff)
                print("Posição: " , arquivo.tell() , ' - ' , 'Tamanho: ' , tamanho)
            arquivo.close()
        except IOError:
            print('Erro ao abrir o arquivo!')

    def writeBinary(self):
        try:
            arquivo = open('copia.jpg', 'w+b')
            arquivo.write(b'hi')
            #arquivo.flush()
            arquivo.close()
        except IOError:
            print('Erro ao abrir o arquivo!')

    
    def readBinaryBlockArray(self, filename, size=1024):
        #pieces = []
        try:
            arquivo = open(filename, 'rb')
            arquivo.seek(0,2)
            tamanho = arquivo.tell()
            arquivo.seek(0)
            while arquivo.tell() < tamanho:
                self.block.append(arquivo.read(size))
            arquivo.close()

        except IOError:
            print("Erro na leitura do arquivo!")

        return self.block





#fileHandler = FileHandler()
#fileHandler.readBinary()
#fileHandler.writeBinary()
#result = fileHandler.readBinaryBlockArray('envio.txt')
#print(result[0])


'''
# Abrindo o arquivo
print('Olá')

try:
    arquivo = open('imageOriginal.jpg', 'rb')
    arquivo.seek(0,2)
    tamanho = arquivo.tell()
    arquivo.seek(0)

    chuck = 1024
    while arquivo.tell() < tamanho:
        buff = arquivo.read(chuck)
        print(buff)
        print("Posição: " , arquivo.tell() , ' - ' , 'Tamanho: ' , tamanho)
    arquivo.close()
except IOError:
    print('Erro ao abrir o arquivo!')
'''



