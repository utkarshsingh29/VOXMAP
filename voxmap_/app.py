import os

from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Example data (replace with your dynamic data source)
markers = [


]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/markers')
def get_markers():
    return jsonify(markers)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# change
from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')
