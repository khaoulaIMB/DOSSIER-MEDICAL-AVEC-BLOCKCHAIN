from solcx import compile_standard, install_solc
import json

# Install a specific version of Solidity
install_solc("0.8.0")

# Load Solidity source code
with open("ContractPatient.sol", "r") as file:
    patient_contract = file.read()

with open("ContractDoctor.sol", "r") as file:
    doctor_contract = file.read()

with open("ContractAudit.sol", "r") as file:
    audit_contract = file.read()

with open("ContractAuthentication.sol", "r") as file:
    authentication_contract = file.read()

with open("ContractStorage.sol", "r") as file:
    storage_contract = file.read()

# Compile all contracts
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {
            "ContractPatient.sol": {"content": patient_contract},
            "ContractDoctor.sol": {"content": doctor_contract},
            "ContractAudit.sol": {"content": audit_contract},
            "ContractAuthentication.sol": {"content": authentication_contract},
            "ContractStorage.sol": {"content": storage_contract},
        },
        "settings": {
            "outputSelection": {
                "*": {
                    "*": [
                        "abi",
                        "metadata",
                        "evm.bytecode",
                        "evm.sourceMap"
                    ]
                }
            }
        },
    },
    solc_version="0.8.0",
)

# Save compiled contracts to a JSON file
with open("compiled_contracts.json", "w") as file:
    json.dump(compiled_sol, file)

print("Smart contracts compiled successfully!")
