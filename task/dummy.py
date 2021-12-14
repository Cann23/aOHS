import sys
import time
from random import randint

print("dummy.py called for: ")
time.sleep(randint(1, 3))
for i in range(len(sys.argv)):
    print(sys.argv[i], " ")
