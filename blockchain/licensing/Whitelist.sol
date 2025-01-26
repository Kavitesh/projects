// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

contract Whitelist {
    address public owner;
    mapping(address => bool) public whitelisted;
    mapping(address => bool) public whitelistAdmins;

    event UserWhitelisted(address indexed user);
    event UserRemovedFromWhitelist(address indexed user);
    event AdminAdded(address indexed admin);
    event AdminRemoved(address indexed admin);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier onlyWhitelistAdmin() {
        require(whitelistAdmins[msg.sender], "Caller is not an admin");
        _;
    }

    modifier onlyWhitelisted() {
        require(whitelisted[msg.sender], "Caller is not whitelisted");
        _;
    }

    constructor() {
        owner = msg.sender;
        whitelistAdmins[owner] = true; // Owner is also an admin by default
    }

    function addAdmin(address _admin) public onlyOwner {
        require(!whitelistAdmins[_admin], "Admin is already added");
        whitelistAdmins[_admin] = true;
        emit AdminAdded(_admin);
    }

    function removeAdmin(address _admin) public onlyOwner {
        require(whitelistAdmins[_admin], "Admin is not added");
        whitelistAdmins[_admin] = false;
        emit AdminRemoved(_admin);
    }

    function addUserToWhitelist(address _user) public onlyWhitelistAdmin {
        require(!whitelisted[_user], "User is already whitelisted");
        whitelisted[_user] = true;
        emit UserWhitelisted(_user);
    }

    function removeUserFromWhitelist(address _user) public onlyWhitelistAdmin {
        require(whitelisted[_user], "User is not whitelisted");
        whitelisted[_user] = false;
        emit UserRemovedFromWhitelist(_user);
    }

    function isUserWhitelisted(address _user) public view returns (bool) {
        return whitelisted[_user];
    }

    function allowAccess() public view onlyWhitelisted returns (bool) {
        return true;
    }
}
