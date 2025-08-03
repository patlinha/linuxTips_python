#!/usr/bin/env python3

import os
import sys
import time
import logging

log = logging.Logger("errors")

#EAFP - Easy to Ask Forgiveness than permission

def try_to_open_a_file(filepath, retry=1):
    """Tries to open a file, if error, retries n times"""
    for attempt in range(1, retry + 1):
        try:
            return open(filepath).readlines() #FileNotFoundError
        except FileNotFoundError as e:
            log.error("ERRO: %s",e)
            time.sleep(2)
        else:
            print("Sucesso!!")
        finally:
            print("Execute isso sempre...")
    return []

for line in try_to_open_a_file("names.txt", retry=5):
    print(line)

'''
try:
    print(names[3])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
'''