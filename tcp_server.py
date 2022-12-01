import socket
import logging
from threading import Thread

IP = '0.0.0.0'
PORT = 9998

def main():
    logging.basicConfig(filename='output.log',format='{asctime} {levelname} {message}', level=logging.INFO,
                        style='{', datefmt='%Y-%m-%d %H:%M')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    logging.info(f"[*] Listening on {IP}:{PORT}")

    while True:
        #Getting client's scocket, ip, port
        client, address = server.accept()
        client_ip, client_port = address
        logging.info(f"[*] Accepted connection from {client_ip}:{client_port}")
        #Creating client's handler
        client_handler = Thread(target=handle_client, args=(client,))
        #Starting the handler
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        logging.info(f"[*] Received: {request.decode()}")
        sock.send(b"ACK")


if __name__ == "__main__":
    main()