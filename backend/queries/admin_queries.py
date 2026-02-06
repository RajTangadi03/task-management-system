# Admin table related CRUD operations

create_admin = """
INSERT INTO central_admin (name, age, email, address, password, creation_time)
VALUES ($1, $2, $3, $4, $5, NOW())
RETURNING id;
"""

read_admin = """
SELECT *
FROM central_admin
WHERE id = $1;
"""

read_all_admin = """
SELECT *
FROM central_admin;
"""

update_admin = """
UPDATE central_admin
SET name = $1, password = $2
WHERE id = $3;
"""

delete_admin = """
DELETE FROM central_admin
WHERE id = $1;
"""