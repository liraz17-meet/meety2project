from flask import Flask, render_template, request, redirect, url_for, session
from model import Base, Questions, answers, users


engine = create_engine('sqlite:///fizzBuzz.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

current_directory = os.getcwd()
UPLOAD_FOLDER = os.path.join(current_directory, 'static/uploads')
allowed_extensions = set(['jpg', 'jpeg', 'png'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
def valid_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in allowed_extensions
def upload():
	file = request.files['file']
	if request.method == 'POST' and file and valid_file(file.filename) and session.get('id')!=None:
		path = os.path.join(aoo.config['UPLOAD_FOLDER'], filename)
		file.save(path)
		user = DBsession.query(Users).filter_by(id = session['id']).first()
		description = request.form['description']
		subject = request.form['subject']
		sub_subject = request.form['sub_subject']
		question = Questions(user_id= user.id, subject, file_name = "uploads/" + filename,subject = request.form['subject'], 
		DBsession.add(question)
		DBsession.commit()


		return render_template('homepage.html')

	else:
		redirect(url_for('upload'))
		

if __name__ == '__main__':
	app.run(debug=True)
