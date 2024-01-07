from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Miracle Morning',
        'author': 'Hal Elrod'
    },
    {
        'id': 2,
        'title': 'Harry Potter',
        'author': 'J. K. Rowling'
    },
    {
        'id': 3,
        'title': 'Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones',
        'author': 'James Clear'
    }
]
#GET ALL
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


#GET BY ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

