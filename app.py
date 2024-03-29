from flask import Flask, render_template, request, redirect, url_for
from mongoDB import Mongodb
from models import Book
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/catalog')
def catalog():
    db = Mongodb.get_db()
    books = db.books.find()
    return render_template('catalog.html', books=books)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/edit/<book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    db = Mongodb.get_db()
    book = db.books.find_one({'_id': ObjectId(book_id)})

    if request.method == 'POST':
        ISBN = int(request.form['ISBN'])
        Title = request.form['Title']
        AuthorID = int(request.form['AuthorID'])
        GenreID = int(request.form['GenreID'])
        TagID = int(request.form['TagID'])
        BookType = request.form['BookType']
        Series = request.form['Series']
        BookNumber = int(request.form['BookNumber'])
        Edition = request.form['Edition']

        db.books.update_one(
            {'_id': ObjectId(book_id)},
            {'$set': {
                'ISBN': ISBN,
                'Title': Title,
                'AuthorID': AuthorID,
                'GenreID': GenreID,
                'TagID': TagID,
                'BookType': BookType,
                'Series': Series,
                'BookNumber': BookNumber,
                'Edition': Edition
            }}
        )

        return redirect(url_for('catalog'))

    return render_template('edit_book.html', book=book)

@app.route('/delete/<book_id>')
def delete_book(book_id):
    db = Mongodb.get_db()
    db.books.delete_one({'_id': ObjectId(book_id)})
    return redirect(url_for('catalog'))

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        ISBN = int(request.form['ISBN'])
        Title = request.form['Title']
        AuthorID = int(request.form['AuthorID'])
        GenreID = int(request.form['GenreID'])
        TagID = int(request.form['TagID'])
        BookType = request.form['BookType']
        Series = request.form['Series']
        BookNumber = int(request.form['BookNumber'])
        Edition = request.form['Edition']

        book = Book(
            ISBN=ISBN,
            Title=Title,
            AuthorID=AuthorID,
            GenreID=GenreID,
            TagID=TagID,
            BookType=BookType,
            Series=Series,
            BookNumber=BookNumber,
            Edition=Edition
        )

        db = Mongodb.get_db()
        db.books.insert_one(book.__dict__)

        return redirect(url_for('catalog'))

    return render_template('add_book.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search_term']
        db = Mongodb.get_db()
        books = db.books.find({'$or': [
            {'Title': {'$regex': search_term, '$options': 'i'}},
            {'Series': {'$regex': search_term, '$options': 'i'}},
            {'Edition': {'$regex': search_term, '$options': 'i'}}
        ]})
        return render_template('search_results.html', books=books, search_term=search_term)

    return redirect(url_for('catalog'))

if __name__ == '__main__':
    app.run(debug=True)