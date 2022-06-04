import socket
import threading
import pyfirmata


board = pyfirmata.Arduino("/dev/cu.usbmodem144301")


LED_pin_red = board.get_pin('d:13:o')
LED_pin_yellow = board.get_pin('d:12:o')
LED_pin_blue = board.get_pin('d:11:o')
LED_pin_green = board.get_pin('d:10:o')

HEADER = 64
PORT = 5050
SERVER = "10.0.0.237"
ADDR = (SERVER, PORT)
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

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                LED_pin_red.write(0)
                connected = False

            elif msg == ONON1:
                LED_pin_red.write(1)
            elif msg == OFFOFF1:
                LED_pin_red.write(0)
            elif msg == ONON2:
                LED_pin_yellow.write(1)
            elif msg == OFFOFF2:
                LED_pin_yellow.write(0)
            elif msg == ONON3:
                LED_pin_blue.write(1)
            elif msg == OFFOFF3:
                LED_pin_blue.write(0)
            elif msg == ONON4:
                LED_pin_green.write(1)
            elif msg == OFFOFF4:
                LED_pin_green.write(0)
            elif msg == ALLON:
                LED_pin_red.write(1)
                LED_pin_yellow.write(1)
                LED_pin_blue.write(1)
                LED_pin_green.write(1)
            elif msg == ALLOFF:
                LED_pin_red.write(0)
                LED_pin_yellow.write(0)
                LED_pin_blue.write(0)
                LED_pin_green.write(0)

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
