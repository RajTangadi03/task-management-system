# manager: id | name | pass | assigned_tasks | completed_tasks |

create_manager = """
INSERT INTO manager (name, password)
VALUES ($1, $2)
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