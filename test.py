from flask import Flask, send_from_directory
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('lab1.html')
@app.route('/img/<path:filename>')
def custom_static(filename):
    return send_from_directory('img', filename)
if __name__ == "__main__":
	app.run(host='localhost', port=5000, debug=True)