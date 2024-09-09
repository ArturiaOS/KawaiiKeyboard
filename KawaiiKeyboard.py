import keyboard
import pygame


audio_library = ["SPACE", "TAB", "BACKSPACE",
                 "A", "B", "C", "D", "E", "F", "G",
                 "H", "I", "J", "K", "L", "M", "N",
                 "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]


def audio_exist_checker(input):
    return input in audio_library

def audio_player(input):
    if audio_exist_checker(input):
        pygame.mixer.Sound("Library/Audios/" + input + ".wav").play()

def run():
    pygame.init()
    print("\nRunning...\nPress ESC to exit.")

    pressed_keys = set()
    while True:
        key = keyboard.read_key().upper()
        if key == "ESC":
            break
        if key not in pressed_keys:
            pressed_keys.add(key)
            audio_player(key)
        elif not keyboard.is_pressed(key):
            pressed_keys.remove(key)