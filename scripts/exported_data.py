from web3 import Web3
import pickle
CONTRACT_ADDRESS = ""
CONTRACT_ABI = ""
addr = open('address','rb')
CONTRACT_ADDRESS = pickle.load(addr)
abi = open('abi','rb')
CONTRACT_ABI = pickle.load(abi)

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
eth = w3.eth

tkn = eth.contract(address = CONTRACT_ADDRESS,abi=CONTRACT_ABI)
accounts = eth.accounts


    


