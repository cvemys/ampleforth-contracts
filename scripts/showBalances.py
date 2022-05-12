#!/usr/bin/python
from web3 import Web3
from exported_data import *
import colors
def blank_space():
    print()
    print()

print("============\t Ethereum Balances \t ============")
for acc in accounts:
    bal = eth.get_balance(account = acc) / (10**18)
    print(f'{colors.OKGREEN}{acc}{colors.ENDC} : {colors.OKCYAN}{bal}{colors.ENDC}')
print("======================================================")
blank_space()
print("============\t Fragment Token Balances \t ============")
for acc in accounts:
    bal = tkn.functions.balanceOf(acc).call()
    print(f'{colors.OKGREEN}{acc}{colors.ENDC} : {colors.OKCYAN}{bal}{colors.ENDC}')
print("======================================================")
