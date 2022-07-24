import socket
from request import Request
import json
from views import build_json_response, handle_users, handle_posts


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', 9291))
    server.listen()

    while True:
        client_connection, _client_address = server.accept()
        client_request = Request(client_connection)
        if client_request.parsed_request['uri'] == '/':
            client_connection.send(build_json_response(json.dumps({"val": "hello world"})).encode())
        elif client_request.parsed_request['uri'] == '/users':
            resp = handle_users(client_request.parsed_request)
            client_connection.send(build_json_response(resp).encode())
        elif client_request.parsed_request['uri'] == '/posts':
            resp = handle_posts(client_request.parsed_request)
            client_connection.send(build_json_response(resp).encode())
        client_connection.shutdown(socket.SHUT_RDWR)
        client_connection.close()


if __name__ == "__main__":
    main()