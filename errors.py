#!/usr/bin/env python3

import os
import sys

#EAFP - Easy to Ask Forgiveness than permission

try:
    raise RuntimeError("Ocorreu um erro") #força a executar o erro sempre
except Exception as e:
    print(str(e))



try:
    names = open("names.txt").readlines() #FileNotFoundError
except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!!")
finally:
    print("Execute isso sempre...")

try:
    print(names[3])
except:
    print("Missing name in this position")
    sys.exit(1)