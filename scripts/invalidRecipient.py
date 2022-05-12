#! /usr/bin/python
from exported_data import *
to = '0x0000000000000000000000000000000000000000'

val = 1000
tx_hash = tkn.functions.transfer(to,val).transact({'from':accounts[0]})
print(f'{val} Tokens transferred from {accounts[0]} to {to} successfully')

