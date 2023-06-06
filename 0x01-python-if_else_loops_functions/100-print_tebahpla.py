#!/usr/bin/python3
x = True
for i in range(90, 64, -1):
    if x:
        i += 32
    print("{}".format(chr(i)), end="")
    x = not x
