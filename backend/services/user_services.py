from dao.user_dao import UserDAO

class UserServices:

    @staticmethod
    def checkPassword(password: str):
        has_low = any('a' <= ch <= 'z' for ch in password)
        has_cap = any('A' <= ch <= 'Z' for ch in password)
        has_num = any('0' <= ch <= '9' for ch in password)

        return has_low and has_cap and has_num
    
    @staticmethod
    async def isCreatable(password):
        isEmail = await UserDAO.find_email(password)
        if isEmail == True:
            raise ValueError("Email ID already Exists.")
        
        if len(password) < 9:
            raise ValueError("Password must have atleast 9 characters.")

        if UserServices.checkPassword(password) == False:
            raise ValueError("A uppercase, lowercase and A Number between 0-9 must be in password.")
        
        return True

    @staticmethod
    async def create_user(data):
        if await UserServices.isCreatable(data.password) == True:
            return await UserDAO.create_user(
                data.name, 
                data.age,
                data.email,
                data.address,
                data.password
            )
    
    @staticmethod
    async def read_user_id(userId):
        # logic to check id

        row = await UserDAO.read_user_id(userId)
        return dict(row) if row else None
    
    @staticmethod
    async def read_all_user():
        rows = await UserDAO.read_all_user()
        return [dict(row) for row in rows]
    
    @staticmethod
    async def update_user(data, userId: int):
        return await UserDAO.update_user(
                data.name, 
                data.age,
                data.email,
                data.address,
                data.password,
                userId
            )
    
    @staticmethod
    async def delete_user(userId: int):
        return await UserDAO.delete_user(userId)
    
    @staticmethod
    async def checkUserPass(name, password):
        return await UserDAO.checkUserPass(name, password)
