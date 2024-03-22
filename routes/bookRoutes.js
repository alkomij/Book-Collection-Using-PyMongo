/** 
 * Book Routes
 * 
 * Defines routes for book-related operations within the application. 
 * This includes endpoints to retrieve all books, fetch a single book by ID, 
 * create a new book, update an existing book, and delete a book. 
 * These routes utilize the BookService to interact with the database, 
 * providing an interface for book management.
 * 
 * Routes:
 * POST / - Create a new book
 * GET / - Get all books
 * GET /:id - Get a single book by its unique ID
 * PUT /:id - Update a book's details by its ID
 * DELETE /:id - Deletes a book by its ID
 * 
 * @version 1.0
 * @author Hasan Siddiqui
*/
const express = require('express');
const router = express.Router();
const path = require('path');

// Universal path to the BookService
const BookService = require(path.join(__dirname, '..', 'services', 'BookService'));

// Route to create a new book
router.post('/', async (req, res) => {
    try {
      const newBook = await BookService.addBook(req.body);
      res.status(201).json(newBook);
    } catch (error) {
      res.status(400).json({ message: error.message });
    }
});

// Route to get all books
router.get('/', async (req, res) => {
  try {
    const books = await BookService.getAllBooks();
    res.json(books);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// Route to get a single book by id
router.get('/:id', async (req, res) => {
  try {
    const book = await BookService.getBookById(req.params.id);
    if (book) {
      res.json(book);
    } else {
      res.status(404).json({ message: 'Book not found' });
    }
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// Route to update a book by id
router.put('/:id', async (req, res) => {
  try {
    const updatedBook = await BookService.updateBook(req.params.id, req.body);
    if (updatedBook) {
      res.json(updatedBook);
    } else {
      res.status(404).json({ message: 'Book not found' });
    }
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Route to delete a book by id
router.delete('/:id', async (req, res) => {
  try {
    const bookDeleted = await BookService.deleteBook(req.params.id);
    if (bookDeleted) {
      res.json({ message: 'Book deleted successfully' });
    } else {
      res.status(404).json({ message: 'Book not found' });
    }
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

module.exports = router;
