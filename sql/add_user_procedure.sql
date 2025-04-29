-- Table creation (optional, if not exists)
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Stored Procedure to add a new user
DELIMITER $$

CREATE PROCEDURE AddUser(IN p_username VARCHAR(100), IN p_email VARCHAR(255))
BEGIN
    INSERT INTO users (username, email)
    VALUES (p_username, p_email);
END$$

DELIMITER ;

-- Example call
-- CALL AddUser('johndoe', 'john@example.com');
