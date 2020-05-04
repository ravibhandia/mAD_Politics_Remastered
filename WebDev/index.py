from flask import Flask,render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mypass@mariadb-diveshop.db-network/MAD_POLITICS'
db = SQLAlchemy(app)
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# Display selected database
@app.route("/database")
def datab():
    result = db.engine.execute("SELECT DATABASE()")
    names = [row[0] for row in result]
    return names[0]

# Display index.html as welcoming page
@app.route("/")
def index():
    ## This is specefically for dynamic display dropdown options based on the database
    # result = db.engine.execute("select DISTINCT(Accomodations) from DEST")
    # accs = []
    #
    # for row in result:
    #     name = {}
    #     name["Accomodations"] = row[0]
    #     accs.append(name)
    # Reading accommodations from database and show unique values on destination dropdown menu in index.html
    return render_template("madPolitics.html")
# , data=accs

### QUERY 1 ###
@app.route("/q1", methods=["POST", "GET"])
def dest():
    # Obtain user selected topN values
    limit = request.args.get('topN')

    # Query
    query = " select rank() over(ORDER BY sum(cost) DESC) as 'Ads Spending Ranking', CONCAT(CANDIDATE.First_name, ' ', CANDIDATE.Last_name), sum(cost) from Advertisement, CANDIDATE WHERE CANDIDATE.Candidate_id = Advertisement.Candidate_id group by CANDIDATE.First_name"
    limit_rank = " LIMIT 0, %s" % limit
    query += limit_rank

    # Execute Query
    result = db.engine.execute(query)

    # Create empty list
    candidate_names = []

    # Iterate rows and append relative column values to a dictionary
    for row in result:
        name = {}
        name["Rank"] = row[0]
        name["Candidate_Name"] = row[1]
        name["Ad_Spending"] = row[2]
        candidate_names.append(name)          # Append this dictionary to list

    return render_template('q1.html',ad_spending_rank=candidate_names)

# # methods indicates a action in html
# @app.route("/destinations", methods=["POST", "GET"])
# def dest():
#     # Display different queries upon input
#     if request.method == "GET":         # By meeting specific accommodations
#         search = request.args.get('accomodations')  # Obtain user selected/input values
#         result = db.engine.execute("select * from DEST where Accomodations=%s", search)
#     else:                               # Select all from DEST
#         result = db.engine.execute("select * from DEST")
#
#     # Create empty list
#     dest_names = []
#
#     # Iterate rows and append relative column values to a dictionary
#     for row in result:
#        name = {}
#        name["Dest_Name"] = row[1]
#        name["Travel_cost"] = row[12]
#        dest_names.append(name)          # Append this dictionary to list
#
#     return render_template('show_d.html', destinations = dest_names)


# # methods indicates a action in html
# @app.route("/customers", methods=["POST", "GET"])
# def customers():
#     # Execute SQL request
#     result = db.engine.execute("select * from DIVECUST")
#
#     # Create empty list
#     names = []
#
#     # Iterate rows and append relative column values to a dictionary
#     for row in result:
#         name = {}
#         name["Cust_Name"] = row[1]
#         name["City"] = row[3]
#         name["State"] = row[4]
#         # name["Other"] = row[20]       # would obtain sqlalchemy.exc.NoSuchColumnError
#         names.append(name)          # Append this dictionary to list
#
#     return render_template('show_c.html',customers=names)
#
# # Display dynaic name on url and html
# @app.route("/customers/<string:name>/")
# def getMember(name):
#     return render_template('show_c.html',customer=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
