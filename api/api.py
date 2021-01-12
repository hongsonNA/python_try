import flask
from flask import Flask, request, Response, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def checkexit_id(id):
    conn = sqlite3.connect('../db/books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    query = "SELECT * FROM books WHERE"
    to_filter = []
    if id:
        query += ' id=?'
        to_filter.append(id)

    results = cur.execute(query, to_filter).fetchone()
    return results

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('../db/books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()

    return jsonify(all_books)



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('../db/books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

@app.route('/api/insert', methods=['POST'])
def create_task():
    if request.method == 'POST':
        data_reponse = request.get_json()
        author = data_reponse['author']
        title = data_reponse['title']
        published = data_reponse['published']
        first_sentence = data_reponse['first_sentence']

        try:
            connect = sqlite3.connect('../db/books.db')
            with connect as con:
                cur = con.cursor()
                sql = "INSERT INTO books (author,title,published,first_sentence) VALUES (?,?,?,?)"
                data_insert = (author,title,published,first_sentence)
                cur.execute(sql, data_insert)
                con.commit()
                msg = {
                    'status': True,
                    'mess': "Record successfully added"
                }
        except:
            con.rollback()
            msg = {
                'status':False,
                'mess' :"error in insert operation"
            }
        finally:
            con.close()
            return jsonify(msg), 200

@app.route('/api/update', methods=['PUT'])
def update_task():
    if request.method == 'PUT':
        data_reponse = request.get_json()
        id = data_reponse['id']
        author = data_reponse['author']
        title = data_reponse['title']
        published = data_reponse['published']
        first_sentence = data_reponse['first_sentence']
        try:
            conn = sqlite3.connect('../db/books.db')
            with conn as con:
                cur = con.cursor()
                sql = "UPDATE  books set author = ?,  title = ?, published = ?,first_sentence = ? where id = ?"
                data_insert = (author, title, published, first_sentence, id)
                cur.execute(sql, data_insert)
                con.commit()
                msg = "Record successfully updated"
        except:
            con.rollback()
            msg = "error in update operation"
        finally:
            con.close()
        return msg


@app.route('/api/delete/<id>', methods=['DELETE'])
def delete_task(id):
    if request.method == 'DELETE':
        try:
            conn = sqlite3.connect('../db/books.db')
            with conn as con:
                cur = con.cursor()
                sql = "DELETE FROM books where id = ?"
                data_insert = (id)
                cur.execute(sql, data_insert)
                con.commit()
                msg = "Record successfully deleted"
        except:
            con.rollback()
            msg = "error in delete"
        finally:
            con.close()
        return msg
app.run()