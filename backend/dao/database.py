import asyncpg

class Database:
    pool: asyncpg.pool = None

db = Database()

async def connect_db():
    db.pool = await asyncpg.create_pool(
        user="postgres",
        password="1234",
        database="tms",
        host="localhost",
        min_size=5,
        max_size=20
    )

async def close_db():
    await db.pool.close()