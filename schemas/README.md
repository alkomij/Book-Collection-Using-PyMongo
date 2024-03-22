# Schemas Directory

## Overview

This `schemas` directory contains the JSON schema definitions for the data models used in our MongoDB database. These schemas define the structure, constraints, and validation rules for documents within our collections, ensuring data consistency and integrity.

## Files

### `books.json`

- **Description**: Defines the schema for the `books` collection, which stores information about the books available in our library or bookstore. This includes details like title, author, genre, price, and inventory count.
- **Primary Key**: `bookId`
- **Fields**:
  - `title`: String
  - `author`: String
  - `genre`: Array of Strings
  - `price`: Number
  - `description`: String
  - `language`: String
  - `inventoryCount`: Number

### `transactions.json`

- **Description**: Outlines the schema for the `transactions` collection, recording the borrowing and returning of books by users. It includes user and book identifiers, borrow and due dates, and the return status.
- **Primary Key**: `transactionId`
- **Fields**:
  - `transactionId`: String
  - `userId`: String, references `users.json`
  - `bookId`: String, references `books.json`
  - `borrowDate`: Date
  - `dueDate`: Date
  - `returned`: Boolean

### `users.json`

- **Description**: Specifies the schema for the `users` collection, which contains user information, including contact details and membership type.
- **Primary Key**: `userId`
- **Fields**:
  - `userId`: String
  - `name`: String
  - `email`: String
  - `address`: Object (with `street`, `city`, `state`, `zip`)
  - `membershipType`: String

## Usage

These schema files are intended as references for developers and database administrators to understand and maintain the structure of the database collections. They are also useful for validating documents before insertion or updating in the database.

## Contributing

When making changes to the schema files, please ensure that corresponding changes are reflected in the database collections and any related application code. Document any modifications in the project's change log.
