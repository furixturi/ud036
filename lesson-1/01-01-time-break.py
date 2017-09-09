import webbrowser
import time

print("program started on " + time.ctime())
num = 0
while (num < 3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=Dr8-6H3PK3M")
    num += 1
