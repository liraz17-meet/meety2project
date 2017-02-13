from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template('homework.html')

@app.route("/math")
def math():
	return render_template('math.html')


@app.route("/math/geometry")
def geometry():
	return render_template('geometry.html')

@app.route("/upload")
def upload():
	return render_template('upload.html')


if __name__ == '__main__':
	app.run(debug=True)
