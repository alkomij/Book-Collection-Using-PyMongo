from models.user import User

class UserService:

    # addUser()
    @staticmethod
    def addUser(user_data):
        user = User(**user_data)
        user.save()
        return user

    # getAllUsers()
    @staticmethod
    def getAllUsers():
        users = User.objects.all()
        return users

    # getUserById()
    @staticmethod
    def getUserById(user_id):
        user = User.objects.get(id=user_id)
        return user

    # updateUser()
    @staticmethod
    def updateUser(user_id, update_data):
        user = User.objects(id=user_id).update_one(**update_data)
        return user
    
    # deleteUser()
    @staticmethod
    def deleteUser(user_id):
        result = User.objects(id=user_id).delete()
        return result
