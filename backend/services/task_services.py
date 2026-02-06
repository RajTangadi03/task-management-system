from dao.task_dao import TaskDao

class TaskService:

    @staticmethod
    async def createTask(data):
        return await TaskDao.create_task(
            data.title,
            data.description, 
            data.assigned_user_id,
            data.status,
            data.due_date
        )
    
    @staticmethod
    async def read_task_id(taskId: int):
        # logic to check id

        row = await TaskDao.read_task_id(taskId)
        return dict(row) if row else None
    
    @staticmethod
    async def read_all_task():
        rows = await TaskDao.read_all_task()
        return [dict(row) for row in rows]
    
    @staticmethod
    async def updateTask(data, id: int):
        return await TaskDao.update_task(
            data.title,
            data.description, 
            data.assigned_user_id,
            data.status,
            data.due_date,
            data.completion_date,
            id
        )
    
    @staticmethod
    async def deleteTask(id: int):
        return await TaskDao.delete_task(
            id
        )

    # add comment to task