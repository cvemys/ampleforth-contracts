#! /usr/bin/python
from exported_data import *
import colors
import sys
if len(sys.argv) != 2:
    exit(1)
val = int(sys.argv[1])

tx_hash = tkn.functions.rebase(val).transact({'from':accounts[0]})
print(f'_totalSupply = _totalSupply + ({val})')

