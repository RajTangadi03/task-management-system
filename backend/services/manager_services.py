from dao.manager_dao import ManagerDao

class MangerService:

    @staticmethod
    async def create_user(data):
            return await ManagerDao.create_manager(
                data.name, 
                data.age,
                data.email,
                data.address,
                data.password,
                data.creation_time
            )
    
    @staticmethod
    async def read_manager_id(managerId):
        # logic to check id

        row = await ManagerDao.read_user_id(managerId)
        return dict(row) if row else None
    
    @staticmethod
    async def read_all_manager():
        rows = await ManagerDao.read_all_manager()
        return [dict(row) for row in rows]