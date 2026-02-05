# Admin table related CRUD operations

create_admin = """
INSERT INTO admin (name, password)
VALUES ($1, $2)
RETURNING id;
"""

read_admin = """
SELECT *
FROM admin
WHERE id = $1;
"""

read_all_admin = """
SELECT *
FROM admin;
"""

update_admin = """
UPDATE admin
SET name = $1, password = $2
WHERE id = $3;
"""

delete_admin = """
DELETE FROM admin
WHERE id = $1;
"""