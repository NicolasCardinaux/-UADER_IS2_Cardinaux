# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: primes.py
# Compiled at: 2024-04-04 12:22:57
# Size of source mod 2**32: 610 bytes
import os
lower = 1
upper = 50
os.system("clear")
print("Numeros primeos entre %d y %d son: \n" % (lower, upper))
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print("%d " % num)
