# Author: Hasan Siddiqui
# Version: 1.0
# Date: Mar 22, 2024

from mongoengine import Document, StringField, EmbeddedDocument, EmbeddedDocumentField

class Address(EmbeddedDocument):
    street = StringField()
    city = StringField()
    state = StringField()
    zip = StringField()

class User(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    address = EmbeddedDocumentField(Address)
    membershipType = StringField(required=True)

    def get_full_address(self):
        """Returns the full address as a single string."""
        if self.address:
            return f"{self.address.street}, {self.address.city}, {self.address.state}, {self.address.zip}"
        return "Address not provided"

    def update_details(self, update_data):
        """Updates user details based on the provided dictionary."""
        for key, value in update_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()

    meta = {
        'collection': 'users'  # Specifies the collection name in MongoDB
    }
