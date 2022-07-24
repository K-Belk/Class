
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # so you don't have to change ports when restarting
server.bind(('localhost', 9292))
print('Waiting For Connection...')
while True:
    server.listen()

    client_connection, _client_address = server.accept()
    print('New Connection received!')

    data = "<html><body><p>Hello World!</p></body></html>\n"
    client_connection.sendall(data.encode())

    client_connection.close()

# stringafy time for time