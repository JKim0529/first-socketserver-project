import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ONON1 = "!ON1"
OFFOFF1 = "!OFF1"
ONON2 = "!ON2"
OFFOFF2 = "!OFF2"
ONON3 = "!ON3"
OFFOFF3 = "!OFF3"
ONON4 = "!ON4"
OFFOFF4 = "!OFF4"
ALLON = "!ALL ON"
ALLOFF = "!ALL OFF"

SERVER = "10.0.0.237"
ADDR = (SERVER, PORT)
online = True

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


# Messages:
disconnecting = ["disconnect", "quit", "bye", "goodbye"]
on = ["on", "turn on", "turn it on", "turn on light", "light on"]
off = ["off", "turn off", "turn it off", "turn off light", "light off"]
allall = ["all", "everything"]
yesyes = ["y", "yes"]
nono = ["n", "no"]


def msg_check(message, cat):
    message = message.lower()

    if message in cat:
        return True
    else:
        return False


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


def turn_on():
    msg = input("Which one do you turn on?: ")

    if msg == "1":
        send(ONON1)
    elif msg == "2":
        send(ONON2)
    elif msg == "3":
        send(ONON3)
    elif msg == "4":
        send(ONON4)
    elif msg_check(msg, allall):
        send(ALLON)
    else:
        send("Invalid field")


def turn_off():
    msg = input("Which one do you turn off?: ")

    if msg == "1":
        send(OFFOFF1)
    elif msg == "2":
        send(OFFOFF2)
    elif msg == "3":
        send(OFFOFF3)
    elif msg == "4":
        send(OFFOFF4)
    elif msg in allall:
        send(ALLOFF)
    else:
        send("Invalid field")


send("Hello World!")


while online:
    msg = input("enter msg: ")
    if msg_check(msg, on):
        turn_on()
    elif msg_check(msg, off):
        turn_off()
    elif msg_check(msg, disconnecting):
        response = input("Are you sure?: ")

        if msg_check(response, yesyes):
            send(DISCONNECT_MESSAGE)
            online = False
        elif msg_check(response, nono):
            pass
        else:
            send("Invalid entry")
    else:
        send(msg)
