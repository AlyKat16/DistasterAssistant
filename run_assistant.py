# Author: Carter Brown
from Assistant import Assistant

agent = Assistant()

while 1:
    msg = input()

    if msg == "exit":
        print("Exiting...")
        break
    elif msg == "":
        pass