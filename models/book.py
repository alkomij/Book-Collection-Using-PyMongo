# Author: Hasan Siddiqui
# Version: 1.0
# Date: Mar 22, 2024

from mongoengine import Document, StringField, ListField, FloatField, IntField

class Book(Document):
    title = StringField(required=True)
    author = StringField(required=True)
    genre = ListField(StringField())
    price = FloatField(required=True)
    description = StringField(required=True)
    language = StringField(required=True)
    inventoryCount = IntField(required=True)

    # Instance method to check if a book is available (inventory count > 0)
    def is_available(self):
        return self.inventoryCount > 0

    # Instance method to display book info in a formatted string
    def display_info(self):
        genres = ", ".join(self.genre)
        return f"{self.title} by {self.author} - {genres} - ${self.price:.2f}"

    meta = {
        'collection': 'books'  # Specifies the collection name in MongoDB
    }
