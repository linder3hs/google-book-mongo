from flask import Blueprint, render_template, url_for, flash, redirect
from app.forms import BookForm
from app.db import db
from app.models.book import Book

book_router = Blueprint('book_router', __name__)

@book_router.route("/")
def index():
  books = db.books.find()
  return render_template("index.html", books=books)


@book_router.route("/crear", methods=['GET', 'POST'])
def create_book():
  book_form = BookForm()

  if book_form.validate_on_submit():
     new_book = Book(
        book_form.title.data,
        book_form.author.data,
        book_form.pages.data,
        book_form.publish_date.data,
        book_form.description.data,
        book_form.isbn.data
     )

     db.books.insert_one(new_book.to_json())

     flash('Libro creado correctamente', 'success')

     return redirect(url_for('book_router.index'))
 
  return render_template("create.html", book_form=book_form)
