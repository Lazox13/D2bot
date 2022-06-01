import keyboard
import pyautogui

while True:
    if keyboard.is_pressed("p"):
        print(pyautogui.position())