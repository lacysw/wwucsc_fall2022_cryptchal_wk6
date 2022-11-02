#!/usr/bin/env python3

from random import randrange

seed = randrange(0, 0xffff)

with open('secret.txt', 'r') as secret_file:
    secret = secret_file.read()

crypt = ''
for char in secret:
    lock = ord(char) + seed
    if lock > 0xffff:
        lock = lock - 0xffff

    lock = lock % 0xffff
    crypt += chr(lock)

with open('output.shd', 'w') as output_file:
    output_file.write(crypt)
