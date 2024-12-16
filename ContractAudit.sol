// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ContractAudit {
    struct Action {
        address user; // Adresse de l'utilisateur (patient ou médecin)
        string actionType; // Type d'action (ex. : "Ajout", "Modification", "Consultation")
        uint256 timestamp; // Horodatage de l'action
        address patient; // Optional: store the associated patient address
    }

    Action[] public actions; // Liste des actions

    // Enregistrer une action
    function logAction(address user, string memory actionType, address patient) public {
        require(user != address(0), "Adresse invalide");
        require(bytes(actionType).length > 0, "Type d'action invalide"); // Optional: actionType validation

        actions.push(Action(user, actionType, block.timestamp, patient));
    }

    // Obtenir le nombre total d'actions
    function getActionCount() public view returns (uint256) {
        return actions.length;
    }

    // Obtenir une action spécifique
    function getAction(uint256 index) public view returns (address, string memory, uint256, address) {
        require(index < actions.length, "Index hors limites");
        Action memory action = actions[index];
        return (action.user, action.actionType, action.timestamp, action.patient);
    }
}
