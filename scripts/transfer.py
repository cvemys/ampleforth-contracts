#! /usr/bin/python
from exported_data import *
import colors
import sys
if len(sys.argv) != 3:
    exit(1)
to = int(sys.argv[1])
val = int(sys.argv[2])
tx_hash = tkn.functions.transfer(accounts[to],val).transact({'from':accounts[0]})
print(f'{val} Tokens transferred from {accounts[0]} to {accounts[to]} successfully')

