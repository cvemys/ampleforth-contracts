#! /usr/bin/python
from web3 import Web3
from solcx import compile_source
import sys
import pickle

def Deploy(filename):
    with open(filename,'r') as f:
        src = f.read()

    compiled_sol = compile_source(src,output_values=['abi','bin'])
    contract_id, contract_interface = compiled_sol.popitem()
    bytecode = contract_interface['bin']
    abi = contract_interface['abi']
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    w3.eth.default_account = w3.eth.accounts[0]
    Token = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = Token.constructor().transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt.contractAddress,abi

fn = sys.argv[1]
(addr,abi) = Deploy(fn)
print(f'Contract {fn} successfully deployed on {addr}')
with open('address','wb') as address:
    pickle.dump(addr,address)

with open('abi','wb') as abif:
    pickle.dump(abi,abif)

    
