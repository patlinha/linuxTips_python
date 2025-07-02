#!/usr/bin/env python3

import os
import sys

#EAFP - Easy to Ask Forgiveness than permission


try:
    1 / 0 #ZeroDivisionError
    names = open("names.txt").readlines() #FileNotFoundError
    print(names.append) #AttributeError
except (FileNotFoundError, ZeroDivisionError) as e:
    print(f"{str(e)}")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] You can't divide any number by 0")
    sys.exit(1)
except AttributeError:
    print("[Error] This is a list not an object")
    sys.exit(1)

try:
    print(names[3])
except:
    print("Missing name in this position")
    sys.exit(1)