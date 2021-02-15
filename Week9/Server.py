import socket
import threading

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind(("localhost", 8080))
server.listen(5)


users = []

def sendAll(message):
    for user in users:
        user.send(message)

def user_messages(user):
    print("ksdnkjsd")
    while True:
        message = user.recv(2048)
        print(f"Message: {message}")
        sendAll(message)


def startServer():
    while True:
        newUser, address = server.accept()
        print(f"Successfully connected!!{newUser}")
        newUser.send("Successfully connected!!".encode("UTF-8"))
        users.append(newUser)
        myThread = threading.Thread(target=user_messages,args=(newUser,))
        myThread.start()


if __name__ == '__main__':
    startServer()
