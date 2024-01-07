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

#PUT
@app.route('/books/<int:id>',methods=['PUT'])
def edit_book_by_id(id):
    edited_book = request.get_json()
    for index,book in enumerate(books):
        if book.get('id') == id:
            books[index].update(edited_book)
            return jsonify(books[index])


#POST
@app.route('/books',methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)

    return jsonify(books)

#DELETE
@app.route('/books/<int:id>',methods=['DELETE'])
def delete_book(id):
    for index, book in enumerate(books):
        if(book.get('id') == id):
            del books[index]

            return jsonify(books)


