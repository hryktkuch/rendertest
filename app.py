from flask import Flask
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = 'database.db'
app = Flask(__name__)

@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_books = con.execute('SELECT title, author FROM books').fetchall()
    con.close()

    books=[]
    for row in db_books:
        books.append({
            'title': row[0],
            'author': row[1]
        })

    return render_template(
        'index.html',
        books=books
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )

@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    author = request.form['author']

    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
    con.commit()
    con.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()