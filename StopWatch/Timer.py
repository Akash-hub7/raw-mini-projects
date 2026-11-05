import time 
from sound import play_alarm

seconds = int(input("Enter the number of seconds to wait: "))

while seconds >=0:
    mins,secs = divmod(seconds,60)
    print(f"{mins:02d}:{secs:02d}", end="\r")
    time.sleep(1)
    seconds-=1

print("\n  Time Up!!!!")
play_alarm()