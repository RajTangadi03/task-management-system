# User table related CRUD operations

read_user_id = """
SELECT * 
FROM user
WHERE id = $1;
"""

read_all_user = """
SELECT * 
FROM user;
"""

create_user = """
INSERT INTO user (name, password)
VALUES ($1, $2)
RETURNING id;
"""

update_user = """
UPDATE user
SET name = $1, password = $2
WHERE id = $3;
"""

delete_user = """
DELETE FROM user
WHERE id = $1;
"""