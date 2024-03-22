const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  address: {
    street: String,
    city: String,
    state: String,
    zip: String
  },
  membershipType: { type: String, required: true }
});

/** 
 * The UserClass represents a user with information such as address and details.
 * This class provides methods to retrieve the full address as a single string and to update user details.
 * 
 * @version 1.0
 * @author Hasan Siddiqui
*/
class UserClass {
  // Instance method to return full address as a single string
  getFullAddress() {
    return `${this.address.street}, ${this.address.city}, ${this.address.state}, ${this.address.zip}`;
  }

  // Instance method to update user details
  async updateDetails(updateData) {
    Object.assign(this, updateData);
    await this.save();
  }
}

// Load class methods into the schema
userSchema.loadClass(UserClass);

const User = mongoose.model('User', userSchema);

module.exports = User;
