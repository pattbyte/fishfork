import random
import time

print("\033[36mCRNG v1.0\033[0m")
time.sleep(0.5)
print("by pattbyte")
time.sleep(1.25)
print()
print("\033[32mWelcome to CRNG!\033[0m")
time.sleep(1)
print("Press [enter] to start rolling!")
print("> Use 'stats' for your statistics.")
print()
roll_counter=0
while True:
  roll = input()
  if roll == "":
    roll_counter+=1
    rf = open("CRNG_rolls.txt","w")
    rf.write(roll_counter)
    rf.close()
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
  elif roll == "stats":
    print()
    print("\033[37m> STATS\033[0m")
    print(f"Rolls: {roll_counter}")
