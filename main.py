import pyautogui as gui
from time import sleep


def _start():
    print('Enter information carefully.')
    n = int(input("How much time you want to send ? (500-5000)"))
    if (n < 500):
        print("Sorry! Invalid message count")
        _start()
    else:
        letsContinue()


def letsContinue():
    name = input("Enter name whom you want to send message(as per your whatsapp contacts) : ")
    message = input("What you want to send in message ? ")
    print("Wait I'm working ....")
    sleep(2)
    gui.press('win')
    sleep(2)
    gui.write('whatsapp')
    sleep(5)
    gui.press('enter')
    sleep(5)
    gui.hotkey('ctrl', 'f')
    gui.write(name)
    sleep(5)
    gui.press('enter')
    sleep(2)
    for x in range(0, _start()):
        gui.write(message)
        gui.press('enter')
        sleep(3)


if (_start() < 500):
    _start()
else:
    letsContinue()
