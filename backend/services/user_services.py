from dao.user_dao import UserDAO

class userServices:

    @staticmethod
    async def create_user(data):
        # logic to check name and password

        return await UserDAO.create_user(
            data.name, 
            data.password
        )
    
    @staticmethod
    async def read_user_id(userId):
        # logic to check id

        row = UserDAO.read_user_id(userId)

        return dict(row) if row else None