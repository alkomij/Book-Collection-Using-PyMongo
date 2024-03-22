from pymongo import MongoClient, ASCENDING, DESCENDING
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

# Indexing

# Create index on authors' last names
authors_col.create_index([('LastName', ASCENDING)])

# Create index on books' titles
books_col.create_index([('Title', ASCENDING)])

# Create index on sales' start and end dates
sales_col.create_index([('StartDate', ASCENDING), ('EndDate', ASCENDING)])

# Aggregation

# Get the total number of books for each author
def get_books_count_by_author():
    pipeline = [
        {
            '$group': {
                '_id': '$AuthorID',
                'totalBooks': {'$sum': 1}
            }
        },
        {
            '$lookup': {
                'from': 'authors',
                'localField': '_id',
                'foreignField': '_id',
                'as': 'author'
            }
        },
        {
            '$unwind': '$author'
        },
        {
            '$project': {
                '_id': 0,
                'author.FirstName': 1,
                'author.LastName': 1,
                'totalBooks': 1
            }
        }
    ]
    result = books_col.aggregate(pipeline)
    return result

# Get the total sales for each sale type
def get_total_sales_by_type():
    pipeline = [
        {
            '$group': {
                '_id': '$SaleType',
                'totalSales': {'$sum': 1}
            }
        }
    ]
    result = sales_col.aggregate(pipeline)
    return result

