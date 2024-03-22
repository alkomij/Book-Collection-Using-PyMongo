# Author: Hasan Siddiqui
# Version: 1.0
# Date: Mar 22, 2024

from datetime import datetime
from mongoengine import Document, ReferenceField, DateTimeField, BooleanField
from .book import Book
from .user import User

class Transaction(Document):
    userId = ReferenceField(User, required=True)
    bookId = ReferenceField(Book, required=True)
    borrowDate = DateTimeField(default=datetime.utcnow)
    dueDate = DateTimeField(required=True)
    returned = BooleanField(default=False)

    # Instance method to check if a transaction is overdue
    def is_overdue(self):
        return not self.returned and datetime.utcnow() > self.dueDate

    # Instance method to mark the transaction as returned
    def mark_as_returned(self):
        self.returned = True
        self.save()

    meta = {
        'collection': 'transactions'  # Specifies the collection name in MongoDB
    }
