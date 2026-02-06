from .database import db
from queries import manager_queries as manager_qurs

class ManagerDao:

    @staticmethod
    async def create_manager(name, age, email, address, password):
        async with db.pool.acquire() as conn:
            return await conn.fetchval(
                manager_qurs.create_manager,
                name,
                age,
                email,
                address,
                password
            )
        
    @staticmethod
    async def read_manager_id(managerId):
        async with db.pool.acquire() as conn:
            row = await conn.fetchrow(manager_qurs.read_manager_id, managerId)
            return dict(row) if row else None
        
    @staticmethod
    async def read_all_manager():
        async with db.pool.acquire() as conn:
            rows = await conn.fetch(manager_qurs.read_all_manager)
            return [dict(row) for row in rows]
        
    @staticmethod
    async def update_manager(name, age, email, address, password, id: int):
        async with db.pool.acquire() as conn:
            return await conn.fetchval(
                manager_qurs.update_manager,
                name,
                age,
                email,
                address,
                password,
                id
            )
        
    @staticmethod
    async def delete_manager(id: int):
        async with db.pool.acquire() as conn:
            return await conn.fetchval(
                manager_qurs.delete_manager, id
            )