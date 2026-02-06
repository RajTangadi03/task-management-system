# User table related CRUD operations

read_user_id = """
SELECT * 
FROM users
WHERE id = $1;
"""

read_all_user = """
SELECT * 
FROM users;
"""

create_user = """
INSERT INTO users (name, age, email, address, password, creation_time)
VALUES ($1, $2, $3, $4, $5, NOW())
RETURNING id;
"""

update_user = """
UPDATE users
SET name = $1, age = $2, email = $3, address = $4, password = $5
WHERE id = $6;
"""

delete_user = """
DELETE FROM users
WHERE id = $1;
"""

find_email = """
SELECT email
FROM users
WHERE email = $1;
"""