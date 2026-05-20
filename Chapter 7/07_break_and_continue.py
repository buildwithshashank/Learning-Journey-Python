for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)

for i in range(100):
    if(i == 34):
        continue # it will skip 34
    print(i)

for i in range(4):
    print("printing")
    if i == 2:
        continue
    print(i)