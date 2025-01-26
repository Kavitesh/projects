// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

contract ConcurrentLicense {
    uint public totalSeats;
    uint public reservedSeats;
    address public owner;

    struct SeatInfo {
        bool isReserved;
        uint startTime;
        uint totalTime;
    }

    mapping(address => SeatInfo) public seatReservations;

    event SeatReserved(address indexed user, uint timestamp);
    event SeatReleased(address indexed user, uint duration);
    event TotalSeatsUpdated(uint newTotalSeats);

    constructor(uint _totalSeats) {
        require(_totalSeats > 0, "Number of seats must be greater than zero");
        totalSeats = _totalSeats;
        reservedSeats = 0;
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier hasSeatAvailable() {
        require(reservedSeats < totalSeats, "No seats available");
        _;
    }

    modifier hasReservedSeat() {
        require(seatReservations[msg.sender].isReserved, "You do not have a reserved seat");
        _;
    }

    function reserveSeat() public hasSeatAvailable {
        require(!seatReservations[msg.sender].isReserved, "You already have a reserved seat");
        
        seatReservations[msg.sender] = SeatInfo(true, block.timestamp, 0);
        reservedSeats += 1;
        emit SeatReserved(msg.sender, block.timestamp);
    }

    function releaseSeat() public hasReservedSeat {
        SeatInfo storage seat = seatReservations[msg.sender];
        seat.isReserved = false;
        uint duration = block.timestamp - seat.startTime;
        seat.totalTime += duration;

        reservedSeats -= 1;
        emit SeatReleased(msg.sender, duration);
    }

    function checkReservation() public view returns (bool) {
        SeatInfo storage seat = seatReservations[msg.sender];
        return seat.isReserved;
    }

    function availableSeats() public view returns (uint) {
        return totalSeats - reservedSeats;
    }

    function getSeatUsageTime(address user) public onlyOwner view returns (uint) {
        return seatReservations[user].totalTime;
    }

    function updateTotalSeats(uint _newTotalSeats) public onlyOwner {
        require(_newTotalSeats >= reservedSeats, "New total seats must be greater than or equal to reserved seats");
        require(_newTotalSeats >= totalSeats - (totalSeats - reservedSeats), "Cannot reduce seats below the number of reserved seats");
        totalSeats = _newTotalSeats;
        emit TotalSeatsUpdated(_newTotalSeats);
    }
}
