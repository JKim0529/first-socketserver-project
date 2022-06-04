from guizero import App, Text, TextBox, PushButton, Picture
import pyfirmata


board = pyfirmata.Arduino("/dev/cu.usbmodem144301")

LED_pin_red = board.get_pin('d:13:o')
LED_pin_yellow = board.get_pin('d:12:o')
LED_pin_blue = board.get_pin('d:11:o')
LED_pin_green = board.get_pin('d:10:o')


def turn_on1():
    LED_pin_red.write(1)


def turn_on2():
    LED_pin_yellow.write(1)


def turn_on3():
    LED_pin_blue.write(1)


def turn_on4():
    LED_pin_green.write(1)


def turn_off1():
    LED_pin_red.write(0)


def turn_off2():
    LED_pin_yellow.write(0)


def turn_off3():
    LED_pin_blue.write(0)


def turn_off4():
    LED_pin_green.write(0)


def turn_on_all():
    LED_pin_red.write(1)
    LED_pin_yellow.write(1)
    LED_pin_blue.write(1)
    LED_pin_green.write(1)


def turn_off_all():
    LED_pin_red.write(0)
    LED_pin_yellow.write(0)
    LED_pin_blue.write(0)
    LED_pin_green.write(0)


app = App(title="Arduino Light Test")

pic = Picture(app, image="./Pictures/uwlogo.png")

on1 = PushButton(app, text="l1", align="left", command=turn_on1)
off1 = PushButton(app, text="O1", align="left", command=turn_off1)
on2 = PushButton(app, text="l2", align="left", command=turn_on2)
off2 = PushButton(app, text="O2", align="left", command=turn_off2)
on3 = PushButton(app, text="l3", align="left", command=turn_on3)
off3 = PushButton(app, text="O3", align="left", command=turn_off3)
on4 = PushButton(app, text="l4", align="left", command=turn_on4)
off4 = PushButton(app, text="O4", align="left", command=turn_off4)
offAll = PushButton(app, text="ALL OFF", align="right", command=turn_off_all)
onAll = PushButton(app, text="ALL ON", align="right", command=turn_on_all)







app.display()