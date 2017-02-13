# --*--:coding:utf-8 --*--
from flask import Flask, render_template, request, send_from_directory, url_for,redirect
# from werkzeug.utils import secure_filename
import os, sys

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "D:/uploads"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        return render_template("detail.html")


@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    file = request.files['upfile']
    # fname = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    #file_url = url_for('uploaded_file', filename=file.filename)
    return redirect('/showdetail')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/showdetail')
def show_detail():
    entries = [ dict( ulr = app.config['UPLOAD_FOLDER']+'/'+files, name = files ) \
                for files in os.listdir(app.config['UPLOAD_FOLDER'])]
    return render_template("detail.html",entries=entries)


if __name__ == '__main__':
    app.run(debug=True)
