from dao.user_dao import UserDAO

class userServices:

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

        if userServices.checkPassword(password) == False:
            raise ValueError("A uppercase, lowercase and A Number between 0-9 must be in password.")
        
        return True

    @staticmethod
    async def create_user(data):
        if await userServices.isCreatable(data.password) == True:
            return await UserDAO.create_user(
                data.name, 
                data.age,
                data.email,
                data.address,
                data.password,
                data.creation_time
            )
    
    @staticmethod
    async def read_user_id(userId):
        # logic to check id

        row = await UserDAO.read_user_id(userId)

        return dict(row) if row else None