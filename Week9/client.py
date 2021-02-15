import socket
from threading import Thread

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect(("localhost", 8080))

def userMessage():
    while True:
        message = client.recv(2048)
        print(message.decode("UTF-8"))

def sendMessage():
    Thread(target=userMessage).start()
    while True:
        client.send(input("Your message:").encode("UTF-8"))


if __name__ == '__main__':
    sendMessage()