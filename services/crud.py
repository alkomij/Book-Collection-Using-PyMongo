from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB Connection
MongoDB_URI = os.getenv('MONGODB_URI')
client = MongoClient(MongoDB_URI)
db = client['bookstore_db']

# Collections
authors_col = db['authors']
books_col = db['books']
genres_col = db['genres']
tags_col = db['tags']
sales_col = db['sales']
stock_col = db['stock']

# CRUD Operations for Authors

# Create Author
def create_author(first_name, last_name):
    author = {
        'FirstName': first_name,
        'LastName': last_name
    }
    result = authors_col.insert_one(author)
    return result.inserted_id

# Read Authors
def get_authors():
    authors = authors_col.find()
    return authors

# Update Author
def update_author(author_id, first_name, last_name):
    authors_col.update_one({'_id': ObjectId(author_id)}, {'$set': {
        'FirstName': first_name,
        'LastName': last_name
    }})

# Delete Author
def delete_author(author_id):
    authors_col.delete_one({'_id': ObjectId(author_id)})

# CRUD Operations for Books

# Create Book
def create_book(isbn, title, author_id, genre_ids, tag_ids, book_type, series, book_number, edition):
    book = {
        'ISBN': isbn,
        'Title': title,
        'AuthorID': author_id,
        'GenreID': genre_ids,
        'TagID': tag_ids,
        'BookType': book_type,
        'Series': series,
        'BookNumber': book_number,
        'Edition': edition
    }
    result = books_col.insert_one(book)
    return result.inserted_id

# Read Books
def get_books():
    books = books_col.find()
    return books

# Update Book
def update_book(book_id, isbn, title, author_id, genre_ids, tag_ids, book_type, series, book_number, edition):
    books_col.update_one({'_id': ObjectId(book_id)}, {'$set': {
        'ISBN': isbn,
        'Title': title,
        'AuthorID': author_id,
        'GenreID': genre_ids,
        'TagID': tag_ids,
        'BookType': book_type,
        'Series': series,
        'BookNumber': book_number,
        'Edition': edition
    }})

# Delete Book
def delete_book(book_id):
    books_col.delete_one({'_id': ObjectId(book_id)})

# CRUD Operations for Genres

# Create Genre
def create_genre(genre_name):
    genre = {
        'GenreName': genre_name
    }
    result = genres_col.insert_one(genre)
    return result.inserted_id

# Read Genres
def get_genres():
    genres = genres_col.find()
    return genres

# Update Genre
def update_genre(genre_id, genre_name):
    genres_col.update_one({'_id': ObjectId(genre_id)}, {'$set': {
        'GenreName': genre_name
    }})

# Delete Genre
def delete_genre(genre_id):
    genres_col.delete_one({'_id': ObjectId(genre_id)})

# CRUD Operations for Tags

# Create Tag
def create_tag(tag_name, keywords):
    tag = {
        'TagName': tag_name,
        'KeyWords': keywords
    }
    result = tags_col.insert_one(tag)
    return result.inserted_id

# Read Tags
def get_tags():
    tags = tags_col.find()
    return tags

# Update Tag
def update_tag(tag_id, tag_name, keywords):
    tags_col.update_one({'_id': ObjectId(tag_id)}, {'$set': {
        'TagName': tag_name,
        'KeyWords': keywords
    }})

# Delete Tag
def delete_tag(tag_id):
    tags_col.delete_one({'_id': ObjectId(tag_id)})

# CRUD Operations for Sales

# Create Sale
def create_sale(sale_type, sale_price, sale_percent, start_date, end_date, isbns):
    sale = {
        'SaleType': sale_type,
        'SalePrice': sale_price,
        'SalePercent': sale_percent,
        'StartDate': start_date,
        'EndDate': end_date,
        'ISBNs': isbns
    }
    result = sales_col.insert_one(sale)
    return result.inserted_id

# Read Sales
def get_sales():
    sales = sales_col.find()
    return sales

# Update Sale
def update_sale(sale_id, sale_type, sale_price, sale_percent, start_date, end_date, isbns):
    sales_col.update_one({'_id': ObjectId(sale_id)}, {'$set': {
        'SaleType': sale_type,
        'SalePrice': sale_price,
        'SalePercent': sale_percent,
        'StartDate': start_date,
        'EndDate': end_date,
        'ISBNs': isbns
    }})

# Delete Sale
def delete_sale(sale_id):
    sales_col.delete_one({'_id': ObjectId(sale_id)})

# CRUD Operations for Stock

# Create Stock
def create_stock(isbn, price, stock):
    stock_item = {
        'ISBN': isbn,
        'Price': price,
        'Stock': stock
    }
    result = stock_col.insert_one(stock_item)
    return result.inserted_id

# Read Stock
def get_stock():
    stock_items = stock_col.find()
    return stock_items

# Update Stock
def update_stock(stock_id, isbn, price, stock):
    stock_col.update_one({'_id': ObjectId(stock_id)}, {'$set': {
        'ISBN': isbn,
        'Price': price,
        'Stock': stock
    }})

# Delete Stock
def delete_stock(stock_id):
    stock_col.delete_one({'_id': ObjectId(stock_id)})