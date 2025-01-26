// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

contract ValidityCheckToken {
    struct LicenseTerms {
        address userAddress;
        uint256 startDate;
        uint256 endDate;
        bytes32 accessToken;
    }

    constructor(address _userAddress, uint256 _startDate, uint256 _endDate) {
        require(_endDate > _startDate, "End date must be after start date");
        license = LicenseTerms(_userAddress, _startDate, _endDate, bytes32(0));
    }

    function getAccessToken() public returns (bytes32) {
        require(msg.sender == license.userAddress, "Only the registered user can request an access token");
        require(block.timestamp >= license.startDate && block.timestamp <= license.endDate, "License period is not active");

        // Generate a new access token
        license.accessToken = keccak256(abi.encodePacked(license.userAddress, block.timestamp));
        emit AccessTokenGenerated(license.userAddress, license.accessToken);
        return license.accessToken;
    }

    function validateAccessToken(bytes32 _token) public returns (bool) {
        bool isValid = (license.accessToken == _token) && (block.timestamp >= license.startDate && block.timestamp <= license.endDate);
        emit AccessTokenValidated(license.userAddress, isValid);
        return isValid;
    }

    LicenseTerms public license;

    event AccessTokenGenerated(address indexed user, bytes32 accessToken);
    event AccessTokenValidated(address indexed user, bool isValid);
}

