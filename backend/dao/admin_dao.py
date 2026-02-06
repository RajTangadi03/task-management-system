from .user_dao import UserDAO
from .manager_dao import ManagerDao
from .task_dao import TaskDao

class AdminDao:

    @staticmethod
    async def create_user(name, age, email, address, password, creation_time):
        return await UserDAO.create_user(name, age, email, address, password, creation_time)
    
    @staticmethod
    async def create_task(title, description, assigned_user_id, status, due_date, created_date):
        return await TaskDao.create_task(title, description, assigned_user_id, status, due_date, created_date)

    @staticmethod
    async def read_all_task():
        return await TaskDao.read_all_task()

    # add comments to task

    @staticmethod
    async def read_all_user():
        return await UserDAO.read_all_user()
    
    # see all manager

    @staticmethod
    async def create_manager(name, age, email, address, password, creation_time):
        return await ManagerDao.create_manager(name, age, email, address, password, creation_time)