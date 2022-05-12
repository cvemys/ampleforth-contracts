#!/usr/bin/python
from web3 import Web3
from exported_data import *
import colors
import sys

allowedFrom = accounts[int(sys.argv[1])]

print(f"============\t {allowedFrom} 's Allowances \t ============")
for acc in accounts:
    bal = tkn.functions.allowance(allowedFrom,acc).call()
    print(f'{colors.OKGREEN}{acc}{colors.ENDC} : {colors.OKCYAN}{bal}{colors.ENDC}')
print("=====================================================================================")
