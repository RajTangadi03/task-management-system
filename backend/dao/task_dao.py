from .database import db
from queries import task_queries
from datetime import datetime

class TaskDao:

    @staticmethod
    def _prepare_datetime(dt):
        """Helper to convert string/aware datetime to naive datetime for asyncpg"""
        if isinstance(dt, str):
            # Replace 'Z' with UTC offset and parse, then remove tzinfo
            dt = datetime.fromisoformat(dt.replace("Z", "+00:00"))
        if isinstance(dt, datetime) and dt.tzinfo is not None:
            return dt.replace(tzinfo=None)
        return dt

    @staticmethod
    async def create_task(title, description, assigned_user_id, status, due_date):
        if due_date and due_date.tzinfo is not None:
            due_date = due_date.replace(tzinfo=None)
        
        async with db.pool.acquire() as conn:
            return await conn.fetchval(
                task_queries.create_task,
                title,
                description, 
                assigned_user_id,
                status,
                due_date,
                None
            )
        
    @staticmethod
    async def read_task_id(taskId: int):
        async with db.pool.acquire() as conn:
            row = await conn.fetchrow(task_queries.read_task_id, taskId)
            return dict(row) if row else None
        
    @staticmethod
    async def read_taskByUser_id(taskId: int):
        async with db.pool.acquire() as conn:
            row = await conn.fetchrow(task_queries.read_taskByUser_id, taskId)
            return dict(row) if row else None
        
    @staticmethod
    async def read_all_task():
        async with db.pool.acquire() as conn:
            rows = await conn.fetch(task_queries.read_all_task)
            return [dict(row) for row in rows]
        
    @staticmethod
    async def update_task(title, description, assigned_user_id, status, due_date, completion_date, id: int):
        if due_date and due_date.tzinfo is not None:
            due_date = due_date.replace(tzinfo=None)

        # Prepare both dates to be proper naive datetime objects
        due_date = TaskDao._prepare_datetime(due_date)
        completion_date = TaskDao._prepare_datetime(completion_date)

        async with db.pool.acquire() as conn:
            return await conn.fetchval(
                task_queries.update_task,
                title,
                description, 
                assigned_user_id,
                status,
                due_date,
                completion_date,
                id
            )
    
    @staticmethod
    async def delete_task(id: int):
        async with db.pool.acquire() as conn:
            return await conn.fetchval(
                task_queries.delete_task,
                id
            )
    # add comment