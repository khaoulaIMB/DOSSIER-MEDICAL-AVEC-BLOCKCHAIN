// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ContractAuthentication {
    enum UserType { Patient, Doctor }

    struct User {
        string name;
        UserType userType;
        bool registered;
    }

    mapping(address => User) public users;

    // Enregistrer un utilisateur (patient ou médecin)
    function registerUser(string memory name, UserType userType) public {
        require(bytes(name).length > 0, "Nom invalide");
        require(!users[msg.sender].registered, "Utilisateur d\\u00E9j\\u00E0 enregistr\\u00E9");
        

        users[msg.sender] = User(name, userType, true);
    }

    // Mettre à jour les informations d'un utilisateur
    function updateUser(string memory name) public {
        require(users[msg.sender].registered, "Utilisateur non enregistr\\u00E9");
        require(bytes(name).length > 0, "Nom invalide");

        users[msg.sender].name = name;
    }

    // Obtenir les détails d'un utilisateur
    function getUser(address user) public view returns (string memory, UserType, bool) {
        require(users[user].registered, "Utilisateur non enregistr\\u00E9");
        User memory u = users[user];
        return (u.name, u.userType, u.registered);
    }
}
