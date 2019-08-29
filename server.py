# Importa as componentes necessários
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Cria um objeto de autorização
authorizer = DummyAuthorizer()

# Adiciona um usuário informando nome, senha, diretório e permissões
authorizer.add_user('Jones Quito', 'jones1987', 'T:\\UFG\\sisdis1\\serverFTP\\repositorio', perm='elradfmw')

# Permite login anônimo
authorizer.add_anonymous('T:\\UFG\\sisdis1\\serverFTP\\repositorio', perm='elradfmw')

# Cria um manipulador de FTP e define quem é o autorizador desse Manipulador
handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("localhost", 3001), handler)
server.serve_forever()
