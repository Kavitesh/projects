CREATE OR REPLACE PROCEDURE add_user(p_username VARCHAR, p_email VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO users (username, email)
    VALUES (p_username, p_email);
END;
$$;

-- Call it like this
-- CALL add_user('johndoe', 'john@example.com');
