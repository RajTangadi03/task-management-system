from queries import user_queries as user_qur
from .database import db

class UserDAO:

    @staticmethod
    async def create_user(name, age, email, address, password):
        async with db.pool.acquire() as conn:
            return await conn.fetchval(
                user_qur.create_user,
                name, 
                age,
                email,
                address,
                password
            )
        
    @staticmethod
    async def read_user_id(userId: int):
        async with db.pool.acquire() as conn:
            row = await conn.fetchrow(user_qur.read_user_id, userId)
            return dict(row) if row else None
        
    @staticmethod
    async def read_all_user():
        async with db.pool.acquire() as conn:
            rows = await conn.fetch(user_qur.read_all_user)
            return [dict(row) for row in rows]
        
    
