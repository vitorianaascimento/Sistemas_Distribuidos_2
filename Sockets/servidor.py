import socket

# cria um objeto socket UDP
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind(('127.0.0.1', 7896))

    #client_socket.listen(1)
    conexao, endereco = client_socket.recvfrom(1024)

    print("Conectado com o cliente!")
    mensagem = conexao.decode()

    client_socket.sendto('deu certo'.encode(), endereco)

    print(f'mensagem: {mensagem} \n host: {endereco}')

except Exception as err:
    print(err)
