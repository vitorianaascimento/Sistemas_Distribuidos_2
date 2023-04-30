import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.connect(('127.0.0.1', 7896))

server_socket.send("Hello Word".encode())
conexao, endereco = server_socket.recvfrom(1024)
mensagem = conexao.decode()

print(f'mensagem cliente: {mensagem}')