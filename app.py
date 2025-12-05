from flask import Flask, request, jsonify
from models import db, User, Book
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def home():
    return {"message": "Book Store API Running!"}

# ---------------- USERS ---------------- #

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user = User(name=data["name"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added"}), 201


@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    out = [{"id": u.id, "name": u.name, "email": u.email} for u in users]
    return jsonify(out)

# ---------------- BOOKS ---------------- #

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    book = Book(title=data["title"], author=data["author"], price=data["price"])
    db.session.add(book)
    db.session.commit()
    return jsonify({"message": "Book added"}), 201


@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    out = [{"id": b.id, "title": b.title, "author": b.author, "price": b.price} for b in books]
    return jsonify(out)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
