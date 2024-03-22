/**
 * User Routes
 *
 * This module defines the routes for user-related operations in the application. It provides
 * endpoints for creating new users, fetching user details (either all users or a specific user
 * by their ID), updating user information, and deleting users. The routes utilize the UserService
 * to perform the necessary database interactions and business logic.
 *
 * Routes:
 * POST / - Create a new user
 * GET / - Get all users
 * GET /:id - Get a single user by their unique ID
 * PUT /:id - Update a user's information by their ID
 * DELETE /:id - Delete a user by their ID
 *
 * @version 1.0
 * @author Hasan Siddiqui
 */

const express = require('express');
const router = express.Router();
const path = require('path');

// Universal path to the UserService
const UserService = require(path.join(__dirname, '..', 'services', 'UserService'));

// Route to create a new user
router.post('/', async (req, res) => {
  try {
    const newUser = await UserService.createUser(req.body);
    res.status(201).json(newUser);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Route to get all users
router.get('/', async (req, res) => {
    try {
      const users = await UserService.getAllUsers();
      res.json(users);
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  });

// Route to get a single user by id
router.get('/:id', async (req, res) => {
  try {
    const user = await UserService.getUserById(req.params.id);
    if (user) {
      res.json(user);
    } else {
      res.status(404).json({ message: 'User not found' });
    }
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// Route to update a user by id
router.put('/:id', async (req, res) => {
  try {
    const updatedUser = await UserService.updateUser(req.params.id, req.body);
    if (updatedUser) {
      res.json(updatedUser);
    } else {
      res.status(404).json({ message: 'User not found' });
    }
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});

// Route to delete a user by id
router.delete('/:id', async (req, res) => {
  try {
    const userDeleted = await UserService.deleteUser(req.params.id);
    if (userDeleted) {
      res.json({ message: 'User deleted successfully' });
    } else {
      res.status(404).json({ message: 'User not found' });
    }
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

module.exports = router;