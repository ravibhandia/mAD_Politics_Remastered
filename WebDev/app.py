from flask import Flask,render_template,request
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mypass@mariadb-diveshop.db-network/Diveshop'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('madPolitics.html')

@app.route('/profile/<username>')
def profile(username):
	return "Welcome %s" % username

@app.route('/submitForm', methods=['POST'])
def handleReq():
	error = None
	arrow = None
	try:
		name = request.form['name']
		age = request.form['age']
		hasWorked = request.form['hasWorked']
		yrOfExp = request.form['yrOfExp']
		skillSets = request.form.getlist("skillSets")
		print(request.form)
		print(name, age)

		# Read book directory csv and display it if user lack reletive skills
		book_list = list()
		if 'Python' not in skillSets:
			filename = 'Book_Directory_Python.csv'
			data_book_Python = pd.read_csv(filename, header=0)
			book_list += list(data_book_Python.values)
		if 'R' not in skillSets:
			filename = 'Book_Directory_R.csv'
			data_book_R = pd.read_csv(filename, header=0)
			book_list += list(data_book_R.values)

		# check if every variable is valid
		# if (error)


		# major = findMajor(request.form['major'])
		# pass variables to Model

		return render_template("Result.html", name=name, age=age, hasWorked = hasWorked,
		yrOfExp = yrOfExp, skillSets = skillSets, book_list = book_list) #result=modelResult, )
	except:
		error = "Please check if there is any missing entry!"
		arrow = "<="
		return render_template('JobHunting.html', error = error, arrow = arrow)
# # Error Handling
#
# @app.errorhandler(werkzeug.exceptions.BadRequest)
# def handle_bad_request(e):
#     return 'bad request!', 400



# Get the local data passed to HTML
@app.route('/post/<int:book_id>')
def show_post(book_id):
	return "the book id is %s" % book_id

@app.route('/Result/<int:age>', methods=['GET','POST'])
def Result(age):
	return render_template("Result.html", age=age)

    # if request.method == 'POST':
    # 	age = request.form['age']
    # 	return render_template('Result.html', age=age)

    # else:
    # 	return render_template('JobHunting.html')

#Webpage will atuo refresh as debug = true
if __name__ == "__main__":
    app.run(port=7000, debug=True)
