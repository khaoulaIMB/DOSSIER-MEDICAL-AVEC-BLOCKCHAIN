from web3 import Web3
import json

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"  # Ganache RPC Server URL
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
if web3.is_connected():
    print("Connected to Ganache!")
else:
    print("Failed to connect to Ganache")

# Set the default account (first account in Ganache)
web3.eth.default_account = web3.eth.accounts[0]

# Load compiled contracts
with open("compiled_contracts.json", "r") as file:
    compiled_contracts = json.load(file)

# Deploy ContractPatient
patient_abi = compiled_contracts["contracts"]["ContractPatient.sol"]["ContractPatient"]["abi"]
patient_bytecode = compiled_contracts["contracts"]["ContractPatient.sol"]["ContractPatient"]["evm"]["bytecode"]["object"]

print("Deploying ContractPatient...")
ContractPatient = web3.eth.contract(abi=patient_abi, bytecode=patient_bytecode)
tx_hash = ContractPatient.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
contract_patient_address = tx_receipt.contractAddress
print(f"ContractPatient deployed at: {contract_patient_address}")

# Deploy ContractDoctor
doctor_abi = compiled_contracts["contracts"]["ContractDoctor.sol"]["ContractDoctor"]["abi"]
doctor_bytecode = compiled_contracts["contracts"]["ContractDoctor.sol"]["ContractDoctor"]["evm"]["bytecode"]["object"]

print("Deploying ContractDoctor...")
ContractDoctor = web3.eth.contract(abi=doctor_abi, bytecode=doctor_bytecode)
tx_hash = ContractDoctor.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
contract_doctor_address = tx_receipt.contractAddress
print(f"ContractDoctor deployed at: {contract_doctor_address}")

# Deploy ContractAudit
audit_abi = compiled_contracts["contracts"]["ContractAudit.sol"]["ContractAudit"]["abi"]
audit_bytecode = compiled_contracts["contracts"]["ContractAudit.sol"]["ContractAudit"]["evm"]["bytecode"]["object"]

print("Deploying ContractAudit...")
ContractAudit = web3.eth.contract(abi=audit_abi, bytecode=audit_bytecode)
tx_hash = ContractAudit.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
contract_audit_address = tx_receipt.contractAddress
print(f"ContractAudit deployed at: {contract_audit_address}")

# Deploy ContractAuthentication
auth_abi = compiled_contracts["contracts"]["ContractAuthentication.sol"]["ContractAuthentication"]["abi"]
auth_bytecode = compiled_contracts["contracts"]["ContractAuthentication.sol"]["ContractAuthentication"]["evm"]["bytecode"]["object"]

print("Deploying ContractAuthentication...")
ContractAuthentication = web3.eth.contract(abi=auth_abi, bytecode=auth_bytecode)
tx_hash = ContractAuthentication.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
contract_auth_address = tx_receipt.contractAddress
print(f"ContractAuthentication deployed at: {contract_auth_address}")

# Deploy ContractStorage
storage_abi = compiled_contracts["contracts"]["ContractStorage.sol"]["ContractStorage"]["abi"]
storage_bytecode = compiled_contracts["contracts"]["ContractStorage.sol"]["ContractStorage"]["evm"]["bytecode"]["object"]

print("Deploying ContractStorage...")
ContractStorage = web3.eth.contract(abi=storage_abi, bytecode=storage_bytecode)
tx_hash = ContractStorage.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
contract_storage_address = tx_receipt.contractAddress
print(f"ContractStorage deployed at: {contract_storage_address}")

