#Loops

for x in range(1,22):
    print(x)

for x in reversed(range(1,22)):
    print(x)

for x in range(1,22,3):
    print(x)

for x in range(1,22):
    if x ==13:
        continue
    else:
        print(x)

for x in range(1,22):
    if x==13:
        break
    else:
        print(x)