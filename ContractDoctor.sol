// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ContractDoctor {
    struct Permission {
        bool granted;
        uint256 timestamp;
    }

    mapping(address => mapping(address => Permission)) public permissions; // [patient][doctor]

    // Grant permission to a doctor
    function grantPermission(address doctor) public {
        require(doctor != address(0), "Invalid doctor address");
        permissions[msg.sender][doctor] = Permission(true, block.timestamp);
    }

    // Revoke permission
    function revokePermission(address doctor) public {
        require(permissions[msg.sender][doctor].granted, "No permission to revoke");
        permissions[msg.sender][doctor] = Permission(false, block.timestamp);
    }

    // Check if a doctor has permission
    function hasPermission(address patient, address doctor) public view returns (bool) {
        return permissions[patient][doctor].granted;
    }
}
