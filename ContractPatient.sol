// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ContractPatient {
    struct Patient {
        string name;
        uint256 age;
        string medicalRecordHash; // Hash of medical records stored on IPFS
        address patientAddress;   // Ethereum address of the patient
    }

    mapping(address => Patient) public patients;

    // Add or update a patient
    function addOrUpdatePatient(string memory name, uint256 age, string memory medicalRecordHash) public {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(age > 0, "Age must be greater than zero");
        require(bytes(medicalRecordHash).length > 0, "Medical record hash cannot be empty");

        patients[msg.sender] = Patient(name, age, medicalRecordHash, msg.sender);
    }

    // Get patient details
    function getPatient(address patientAddress) public view returns (string memory, uint256, string memory) {
        Patient memory patient = patients[patientAddress];
        return (patient.name, patient.age, patient.medicalRecordHash);
    }
}
