# manager: id | name | pass | assigned_tasks | completed_tasks |

create_manager = """
INSERT INTO manager (name, age, email, address, password, creation_time)
VALUES ($1, $2, $3, $4, $5, NOW())
RETURNING id;
"""

read_manager_id = """
SELECT *
FROM manager
WHERE id = $1;
"""

read_all_manager = """
SELECT *
FROM manager;
"""

update_manager = """
UPDATE manager
SET name = $1, password = $2
WHERE id = $3;
"""

delete_manager = """
DELETE FROM manager
WHERE id = $1;
"""