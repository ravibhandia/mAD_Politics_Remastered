from flask import Flask,render_template,request
#import pandas as pd
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Import database source
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mypass@mariadb-diveshop.db-network/MAD_POLITICS'
db = SQLAlchemy(app)

# Display index.html as welcoming page
@app.route('/')
def index():
	# This is specefically for dynamic display dropdown options based on the database
   result = db.engine.execute("select DISTINCT(CONCAT(CANDIDATE.First_name,' ',CANDIDATE.Last_name)) AS Candidate_Name from CANDIDATE")
   accs = []

   for row in result:
       name = {}
       name["Candidate_Name"] = row[0]
       accs.append(name)
   return render_template('madPolitics.html', canname=accs)

    #return render_template('madPolitics.html')

# Display selected database
@app.route("/database")
def datab():
	# return "welcome"
	result = db.engine.execute("SELECT DATABASE()")
	names = [row[0] for row in result]
	return names[0]



######################### QUERY 4 #############################
@app.route("/q4", methods=["POST", "GET"])
def Query_4():

	topNpf = request.args.get('topNpf')

	#print(canName)
    # Query
	query = "SELECT Platform_name,count(*) as Total\
	FROM Advertisement, Ad_platform\
	WHERE Ad_platform.Platform_id = Advertisement.Platform_id\
	GROUP BY Platform_name\
	ORDER by Total DESC"

	#query += " AND "
	#query += "CONCAT(CANDIDATE.First_name,' ',CANDIDATE.Last_name) = '%s' " % canName
    
    
    # Show poll data of only user specified candidate
    

    # Execute Query
	result = db.engine.execute(query)

    # Create empty list
	platform_names = []

    # Iterate rows and append relative column values to a dictionary
	for row in result:
		name = {}
		name["Platform_name"] = row[0]
		name["Total"] = row[1]
		platform_names.append(name)          # Append this dictionary to list
	
	return render_template('q4.html',pf_rank=platform_names)
	

########################## QUERY 5 #############################
@app.route("/q5", methods=["POST", "GET"])
def Query_5():

	canName = request.args.get('canName')

	print(canName)
    # Query
	query = "SELECT DISTINCT(CONCAT(CANDIDATE.First_name,' ',CANDIDATE.Last_name)) AS Candidate_Name,State.State_name,Polling.Polling_percent\
	FROM CANDIDATE,State,Polling\
	WHERE CANDIDATE.State_id = Polling.State_id AND CANDIDATE.Candidate_id = Polling.Candidate_id AND CANDIDATE.State_id = State.State_id"

	query += " AND "
	query += "CONCAT(CANDIDATE.First_name,' ',CANDIDATE.Last_name) = '%s' " % canName
    
    
    # Show poll data of only user specified candidate
    

    # Execute Query
	result = db.engine.execute(query)

    # Create empty list
	candidate_names = []

    # Iterate rows and append relative column values to a dictionary
	for row in result:
		name = {}
		name["Candidate_Name"] = row[0]
		name["State_name"] = row[1]
		name["Polling_percent"] = row[2]
		candidate_names.append(name)          # Append this dictionary to list
	
	return render_template('q5.html',can_in_home=candidate_names)






if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
