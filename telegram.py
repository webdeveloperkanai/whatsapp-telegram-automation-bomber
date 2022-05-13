import pyautogui as gui
from time import sleep

print('Enter information carefully.')
name = input("Enter name whom you want to send message(as per your telegram contacts) : ")
n = int(input("How much time you want to send ? (500-5000)"))
message = input("What you want to send in message ? ")
print("Wait I'm working ....")
sleep(2)
gui.press('win')
sleep(2)
gui.write('telegram')
sleep(5)
gui.press('enter')
sleep(5)
# gui.hotkey('ctrl','f')
gui.write(name)
sleep(5)
gui.press('enter')
sleep(2)
for x in range(0,n):
    gui.write(message)
    gui.press('enter')
    sleep(3)
