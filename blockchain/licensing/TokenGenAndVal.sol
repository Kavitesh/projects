// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

contract TokenGenAndVal {
    // Mapping from user address to stored token
    mapping(address => bytes32) public tokens;

    // Generate a token based on user address, nonce, licenseTerm, and timestamp
    function generateToken(address _user, uint256 _nonce, string memory _licenseTerm) public returns (bytes32) {
        // Create a unique token based on user address, nonce, licenseTerm, and current timestamp
        bytes32 token = keccak256(abi.encodePacked(_user, _nonce, _licenseTerm));
        tokens[_user] = token;
        return token;
    }

    // Validate the token based on user address, nonce, licenseTerm, and token
    function validateToken(address _user, uint256 _nonce, string memory _licenseTerm, bytes32 _token) public view returns (bool) {
        bytes32 expectedToken = keccak256(abi.encodePacked(_user, _nonce, _licenseTerm));
        return expectedToken == _token && tokens[_user] == _token;
    }
}