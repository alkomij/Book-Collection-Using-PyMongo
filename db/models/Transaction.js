const mongoose = require('mongoose');

const transactionSchema = new mongoose.Schema({
  userId: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  bookId: { type: mongoose.Schema.Types.ObjectId, ref: 'Book', required: true },
  borrowDate: { type: Date, default: Date.now },
  dueDate: { type: Date, required: true },
  returned: { type: Boolean, default: false }
});

/** 
 * The TransactionClass represents a transaction with information such as due date and return status.
 * This class provides methods to check if a transaction is overdue, calculate the number of overdue days,
 * and mark the transaction as returned.
 * 
 * @version 1.0
 * @author Hasan Siddiqui
*/
class TransactionClass {
  // Instance method to check if a transaction is overdue
  isOverdue() {
    const now = new Date();
    return this.returned === false && now > this.dueDate;
  }

  // Instance method to calculate the number of overdue days
  overdueDays() {
    if (!this.isOverdue()) return 0;
    const now = new Date();
    return Math.ceil((now - this.dueDate) / (1000 * 60 * 60 * 24)); // Convert milliseconds to days
  }

  // Instance method to mark the transaction as returned
  markAsReturned() {
    this.returned = true;
    this.returnDate = new Date(); // Assuming you add a returnDate field to your schema
    return this.save();
  }
}

// Load class methods into the schema
transactionSchema.loadClass(TransactionClass);

const Transaction = mongoose.model('Transaction', transactionSchema);

module.exports = Transaction;
