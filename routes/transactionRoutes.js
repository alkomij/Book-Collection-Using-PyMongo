/**
 * Transaction Routes
 * 
 * Defines routes for handling transactions within the application. This includes
 * creating new transactions, fetching transactions for all users or a specific user,
 * and marking transactions as returned. The routes utilize the TransactionService
 * to interact with the database and perform the necessary operations.
 * 
 * Routes:
 * POST / - Create a new transaction
 * GET / - Get all transactions
 * GET /user/:userId - Get all transactions for a specific user
 * PATCH /:id/return - Mark a transaction as returned
 * PUT /:id - Updates a transaction by its ID
 * DELETE /:id - Deletes a transaction by its ID
 * 
 * @version 1.0
 * @author Hasan Siddiqui
 */

const express = require('express');
const router = express.Router();
const path = require('path');

// Universal path to the TransactionService
const TransactionService = require(path.join(__dirname, '..', 'services', 'TransactionService'));

// Route to create a new transaction
router.post('/', async (req, res) => {
  try {
    const newTransaction = await TransactionService.createTransaction(req.body);
    res.status(201).json(newTransaction);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Route to get all transations
router.get('/', async (req, res) => {
    try {
      const transactions = await TransactionService.getAllTransactions();
      res.json(transactions);
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  });

// Route to get all transactions for a user
router.get('/user/:userId', async (req, res) => {
  try {
    const transactions = await TransactionService.getTransactionsByUser(req.params.userId);
    res.json(transactions);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// Route to mark a transaction as returned
router.patch('/:id/return', async (req, res) => {
  try {
    const returnedTransaction = await TransactionService.markAsReturned(req.params.id);
    if (returnedTransaction) {
      res.json(returnedTransaction);
    } else {
      res.status(404).json({ message: 'Transaction not found' });
    }
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// Route to update a book by id
router.put('/:id', async (req, res) => {
    try {
      const updatedTransaction = await TransactionService.updateTransaction(req.params.id, req.body);
      if (updatedTransaction) {
        res.json(updatedTransaction);
      } else {
        res.status(404).json({ message: 'Transaction not found' });
      }
    } catch (error) {
      res.status(400).json({ message: error.message });
    }
  });

// Route to delete a book by id
router.delete('/:id', async (req, res) => {
    try {
      const transactionDeleted = await TransactionService.deleteTransaction(req.params.id);
      if (transactionDeleted) {
        res.json({ message: 'Transaction deleted successfully' });
      } else {
        res.status(404).json({ message: 'Transaction not found' });
      }
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  });

module.exports = router;