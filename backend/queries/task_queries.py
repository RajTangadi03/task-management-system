# task table relalted crud operations

create_task = """
INSERT INTO task (title, description, assigned_user_id, status, due_date, completion_date, created_date)
VALUES ($1, $2, $3, $4, $5, $6, NOW())
RETURNING id;
"""

read_task_id = """
SELECT * 
FROM task 
WHERE id = $1;
"""

read_all_task = """
SELECT * 
FROM task;
"""

update_task = """
UPDATE task
SET title = $1, description = $2, assigned_user_id = $3, status = $4, due_date = $5, completion_date = $6 
WHERE id = $7
RETURNING title;
"""

delete_task = """
DELETE FROM task
WHERE id = $1
RETURNING id;
"""