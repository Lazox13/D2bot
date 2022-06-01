import keyboard as keyboard
import pyautogui as pyautogui
import time

print(pyautogui.size())
wait = 2


def run():
    # Débuter étant dans le cryptarque
    pyautogui.press("f1")  # Personnage
    print("Perso")

    stop()

    pyautogui.moveTo(1000, 70)  # Collection
    print("Collection")
    pyautogui.click()
    time.sleep(wait)

    stop()

    pyautogui.moveTo(900, 325)  # Armure
    print("Armure")
    pyautogui.click()
    time.sleep(wait)

    stop()

    pyautogui.moveTo(550, 830)  # Leveling
    print("Leveling")
    pyautogui.click()
    time.sleep(wait)

    stop()

    pyautogui.moveTo(1800, 830)  # Page de droite
    print("Page de droite")
    pyautogui.click()
    time.sleep(wait)

    stop()

    pyautogui.moveTo(1125, 830)  # Fanion
    print("Fanion")
    for i in range(9):  # Achete les 9 fanions
        pyautogui.click(1125, 830, duration=3.25)
        stop()

    pyautogui.press("esc")  # Triomphe
    print("Triomphe")

    pyautogui.moveTo(1400, 70)  # Personnage
    print("Personnage")
    pyautogui.click()
    time.sleep(wait)

    stop()

    pyautogui.moveTo(1400, 800)  # fanion du perso
    print("Fanion du perso")
    time.sleep(wait / 2)

    stop()

    pyautogui.moveTo(1500, 800, )  # fanion achetée

    stop()

    for i in range(9):  # Démentelle les fanions
        pyautogui.keyDown("f")
        time.sleep(3.25)
        pyautogui.keyUp("f")
        stop()

    # pyautogui.press("esc")  # Cryptarque
    time.sleep(wait)  # Ajouter x2 au wait si c'est short

    for i in range(4):  # Achete fles truc randoms
        pyautogui.moveTo(1400, 380)  # Position à définir sur truc random
        print("Random")
        pyautogui.click()
        time.sleep(wait)
        stop()

    pyautogui.moveTo(1050, 380)  # Position à définir lumen
    print("Lumen")
    pyautogui.click()
    time.sleep(wait)

    stop()


def stop():
    if keyboard.is_pressed('ctrl'):
        pyautogui.moveTo(960, 540)
        exit()


# TEST

def tempoBuy():
    pyautogui.moveTo(1135, 878)  # Fanion
    print("Fanion")
    for i in range(9):  # Achete les 9 fanions
        pyautogui.click(1135, 878, duration=3.25)
        stop()

def tempoSell():
    for i in range(9):  # Démentelle les fanions
        pyautogui.keyDown("f")
        time.sleep(3.25)
        pyautogui.keyUp("f")
        stop()

def tempoRandom():
    for i in range(4):  # Achete fles truc randoms
        pyautogui.moveTo(1377, 378)  # Position à définir sur truc random
        print("Random")
        pyautogui.click()
        time.sleep(2)
        stop()

    pyautogui.moveTo(1377, 378)  # Position à définir lumen
    print("Lumen")
    pyautogui.click()




time.sleep(2)
if __name__ == "__main__":
    while True:
        run()
