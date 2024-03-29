from pymongo import MongoClient

class Mongodb:
    def get_db():
        client = MongoClient("mongodb+srv://imunib:imunibpassword@bookstoreapp-dev.21suk3u.mongodb.net/?retryWrites=true&w=majority&appName=BookStoreApp-Dev")
        db = client["BookStoreApp-Dev"]
        return db