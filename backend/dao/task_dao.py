from .database import db
from queries import task_queries

class TaskDao:

    @staticmethod
    async def create_task(title, description, assigned_user_id, status, due_date, created_date):
        async with db.pool.acquire() as conn:
            return await conn.fetchval(
                task_queries.create_task,
                title,
                description, 
                assigned_user_id,
                status,
                due_date,
                None,
                created_date
            )
        
    @staticmethod
    async def read_task_id(taskId: int):
        async with db.pool.acquire() as conn:
            row = await conn.fetchrow(task_queries.read_user_id, taskId)
            return dict(row) if row else None
        
    @staticmethod
    async def read_all_task():
        async with db.pool.acquire() as conn:
            rows = await conn.fetch(task_queries.read_all_task)
            return [dict(row) for row in rows]
        
    @staticmethod
    async def update_task(title, description, assigned_user_id, status, due_date, completion_date):
        async with db.pool.acquire() as conn:
            return await conn.fetchval(
                task_queries.create_task,
                title,
                description, 
                assigned_user_id,
                status,
                due_date,
                completion_date
            )
        
    # add comment