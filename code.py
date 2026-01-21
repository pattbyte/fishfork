import random
import time

print("CRNG v1.0")
time.sleep(0.5)
print("by pattbyte")
time.sleep(1)
print()
print("Welcome to CRNG!")
time.sleep(0.25)
print("Press [enter] to start rolling!")
while True:
  roll = input()
  if roll == "":
    rdn = randint(1,1000000)
    if rdn < 5:
      print("[???]: 0.0005%")
    if rdn < 10:
      print("[Mythic]: 0.001%")
    if rdn < 100:
      print("[Incredible]: 0.01%")
    if rdn < 1000:
      print("[Gem]: 0.1%")
    if rdn < 10000:
      print("[Rare]: 1%")
    if rdn < 100000:
      print("[Uncommon]: 10%")
    if rdn < 500000:
      print("[Common]: 50%")
    if rdn < 750000:
      print("[Basic]: 75%")
