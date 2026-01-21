import random
import time

print("CRNG v1.0")
time.sleep(0.5)
print("by pattbyte")
time.sleep(1.25)
print()
print("Welcome to CRNG!")
time.sleep(1)
print("Press [enter] to start rolling!")
while True:
  roll = input()
  if roll == "":
    time.sleep(0.1)
    rdn = random.randint(1,1000000)
    if rdn < 5:
      print("\033[33m[???]: 0.0005%\033[0m")
    elif rdn < 10:
      print("\033[31m[Mythic]: 0.001%\033[0m")
    elif rdn < 100:
      print("\033[35m[Incredible]: 0.01%\033[0m")
    elif rdn < 1000:
      print("\033[32m[Gem]: 0.1%\033[0m")
    elif rdn < 10000:
      print("\033[34m[Rare]: 1%\033[0m")
    elif rdn < 100000:
      print("\033[36m[Uncommon]: 10%\033[0m")
    elif rdn < 500000:
      print("\033[90m[Common]: 50%\033[0m")
    elif rdn < 750000:
      print("\033[37m[Basic]: 75%\033[0m")
    elif rdn < 999999:
      print("\033[37m[Dogwater] : 99.9%\033[0m")
