# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    target_host = "127.0.0.1"
    target_port = 9998

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))
    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

    response = client.recv(4096)
    print(response.decode())
    client.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
