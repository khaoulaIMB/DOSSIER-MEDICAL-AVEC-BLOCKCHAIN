// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ContractStorage {
    struct MedicalFile {
        string ipfsHash; // Hachage IPFS du fichier médical
        uint256 timestamp; // Horodatage de la création
    }

    mapping(address => MedicalFile[]) public medicalFiles; // [patient] => Liste des fichiers médicaux

    // Ajouter un nouveau fichier médical
    function addMedicalFile(string memory ipfsHash) public {
        require(bytes(ipfsHash).length > 0, "Hachage IPFS invalide");

        medicalFiles[msg.sender].push(MedicalFile(ipfsHash, block.timestamp));
    }

    // Obtenir les fichiers d'un patient
    function getMedicalFiles(address patient) public view returns (MedicalFile[] memory) {
        return medicalFiles[patient];
    }
}
