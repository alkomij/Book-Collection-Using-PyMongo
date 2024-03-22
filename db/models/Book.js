
const mongoose = require("mongoose");

const bookSchema = new mongoose.Schema({
    title: { type: String, required: true },
    author: { type: String, required: true },
    genre: [{ type: String }],
    price: { type: Number, required: true },
    description: { type: String, required: true },
    language: { type: String, required: true },
    inventoryCount: { type: Number, required: true },
});

/** 
 * The BookClass represents a book with information such as title, author, genre, price, and inventory count.
 * This class provides methods to check if a book is available and to display its information in a formatted string.
 * 
 * @version 1.0
 * @author Hasan Siddiqui
*/
class BookClass {

    // Instance method to check if a book is available (inventory count > 0)
    isAvailable() {
        return this.inventoryCount > 0;
    }

    // Instance method to display book info in a formatted string
    displayInfo() {
        return `${this.title} by ${this.author} - ${this.genre.join(", ")} - $${this.price.toFixed(2)}`;
    }
}

// Load class methods into the schema
bookSchema.loadClass(BookClass);

const Book = mongoose.model("Book", bookSchema);

module.exports = Book;
