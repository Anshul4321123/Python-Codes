import time
import sys

spinner = ['|', '/', '-', '\\','|', '/', '-', '\\']

for i in range(5):  
    for frame in spinner:
        sys.stdout.write('\r' + frame)
        sys.stdout.flush()
        time.sleep(0.1) 
    print("")
    print(f"{i} loop")

print('\nDone!')
