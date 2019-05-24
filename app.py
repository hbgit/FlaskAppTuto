import os
from flask import Flask, redirect, url_for, request, render_template, flash
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import sys

app = Flask(__name__)
app.secret_key = 'S#!@123'

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client['tododb']

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/deleteAll')
def deleteAll():
    db.tododb.drop()
    return redirect(url_for('todo'))


@app.route('/')
def todo():

    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('todo.html', items=items)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/new', methods=['POST'])
@app.route('/new', methods=['GET', 'POST'])
def new():
    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }

    # check if the post request has the file part
    print(request.headers, file=sys.stderr)
    print(request.files, file=sys.stderr)
    if 'photo' not in request.files:
        # flash('No file part')
        error = 'No file part'
        return render_template('todo.html', error=error)
    file = request.files['photo']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        #flash('No selected file')
        error = 'No selected file'
        return render_template('todo.html', error=error)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        item_doc['path_image'] = "uploads/" + str(file.filename)

    db.tododb.insert_one(item_doc)

    return redirect(url_for('todo'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
