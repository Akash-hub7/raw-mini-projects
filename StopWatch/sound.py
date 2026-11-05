import winsound
import time

def play_alarm():
    for _ in range(3):
        winsound.Beep(1000, 700)
        time.sleep(0.2)