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
INSERT INTO users (username, age, email, address, hashed_password, creation_time)
VALUES ($1, $2, $3, $4, $5, NOW())
RETURNING id;
"""

update_user = """
UPDATE users
SET username = $1, age = $2, email = $3, address = $4, hashed_password = $5
WHERE id = $6
RETURNING id;
"""

delete_user = """
DELETE FROM users
WHERE id = $1
RETURNING id;
"""

find_email = """
SELECT email
FROM users
WHERE email = $1;
"""

checkUserPass = """
SELECT id
FROM users
WHERE username = $1 and hashed_password = $2
"""

get_user_by_name = """
SELECT id, username, hashed_password FROM users WHERE username = $1;
"""