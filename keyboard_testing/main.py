import keyboard
import time
while True:
    if keyboard.is_pressed("A"):
        print("a")
        time.sleep(0.1)
    elif keyboard.is_pressed("B"):
        print("b")
        time.sleep(0.1)
    elif keyboard.is_pressed("C"):
        print("c")
        time.sleep(0.1)
    elif keyboard.is_pressed("Esc"):
        break