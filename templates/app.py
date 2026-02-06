from flask import Flask, render_template, request
import os
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    if not f: return "No file uploaded"

    # Save the file
    path = f"uploads/{f.filename}"
    if not os.path.exists('uploads'): os.mkdir('uploads')
    f.save(path)

    # Short bit of code to "read" the CSV
    with open(path, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        row_count = len(rows)

    return f"Success! Uploaded {f.filename} with {row_count} rows of data."

if __name__ == '__main__':
    app.run(debug=True)
