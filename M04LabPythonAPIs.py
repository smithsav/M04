'''
Savannah Smith

M04 Lab Case Study Python API's

Create a CRUD API for a Book. The Book model should have the following parameters:
id
book_name
author
publisher

'''

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
books = [
    {"id": 1, "book_name": "Krull", "author": "Allan Dean Foster", "publisher": "Warner Books"},
    {"id": 2, "book_name": "Pet Sematary", "author": "Stephen King", "publisher": "Doubleday."}
]

# CRUD Operations

# Create
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    books.append(new_book)
    return jsonify(new_book), 201

# Read all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Read single book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Update
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book.update(request.json)
            return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Delete
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for index, book in enumerate(books):
        if book['id'] == book_id:
            del books[index]
            return jsonify({'message': 'Book deleted'})
    return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
