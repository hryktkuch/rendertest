from flask import Flask
from flask import render_template
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

if __name__ == '__main__':
    app.run()