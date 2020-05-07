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


################################# QUERY 1 ####################################
@app.route("/q1", methods=["POST", "GET"])
def Query_1():
    # Query
    query = "\
    SELECT RANK() OVER(ORDER BY sum(cost) DESC) AS 'Ads Spending Ranking',\
           CONCAT(CANDIDATE.First_name, ' ', CANDIDATE.Last_name) AS Candidate_Name,\
           sum(cost) AS Total_Cost\
           FROM Advertisement, CANDIDATE, Affiliates\
           WHERE CANDIDATE.Candidate_id = Affiliates.Candidate_id AND\
                 Advertisement.Group_id = Affiliates.Affiliate_id\
           GROUP BY Candidate_Name\
           ORDER BY 'Ads Spending Ranking' "

    # Obtain user selected topN values
    limit = request.args.get('topN')
    # Show only the topN result
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

    return render_template('q1.html',ad_spending_rank=candidate_names, limit = limit)
################################# QUERY 1 ####################################


################################# QUERY 2 ####################################
@app.route("/q2", methods=["POST", "GET"])
def Query_2():
    #Query
    query = "\
    WITH vote_rank as (\
    SELECT State_id,\
            RANK() over(partition by State_id order by Polling_percent DESC) AS Polling_rank,\
            Candidate_id,\
            Polling_percent,\
            LEAD(Polling_percent, 1) OVER(PARTITION BY State_id ORDER BY Polling_percent DESC) AS Runner_up_poll\
    FROM Polling)\
    SELECT State.state_name,\
            CONCAT(First_name, ' ', Last_name) AS Candidate_Name,\
            Polling_percent,\
            (Polling_percent - Runner_up_poll) AS 'Percent Lead'\
    FROM vote_rank, CANDIDATE, State\
    WHERE vote_rank.Polling_rank = 1 AND\
            vote_rank.Candidate_id = CANDIDATE.Candidate_id AND\
            vote_rank.State_id = State.State_id "

    # Obtain user selected State values
    state = request.args.get('state_selection')
    # Show poll data of only user specified state
    if state != "All":
        query += " AND "
        query += " State.State_abbreviation = '%s' " % state

    query += " ORDER BY State_name "

    # Execute Query
    result = db.engine.execute(query)

    # Create empty list
    Poll_lead_per_state = []

    # Iterate rows and append relative column values to a dictionary
    for row in result:
        name = {}
        name["State_Name"] = row[0]
        name["Candidate_Name"] = row[1]
        name["Lead_poll"] = row[2]
        name["Percent_Lead"] = row[3]
        Poll_lead_per_state.append(name)          # Append this dictionary to list

    return render_template('q2.html',State_poll_lead=Poll_lead_per_state, state=state)
################################# QUERY 2 ####################################

################################# QUERY 3 ####################################
@app.route("/q3", methods=["POST", "GET"])
def Query_3():
    # Query
    query = "\
    WITH State_lead AS ( \
    SELECT State_name,\
            RANK() OVER(PARTITION BY Polling.State_id ORDER BY Polling_percent DESC) AS Polling_rank,\
            CONCAT(CANDIDATE.First_name, ' ', CANDIDATE.Last_name) AS Candidate_name,\
            Polling_percent,\
            Delegates\
    FROM Polling\
    LEFT JOIN State USING (State_id)\
    RIGHT JOIN CANDIDATE USING (Candidate_id)\
   )\
    SELECT ROW_NUMBER() OVER(ORDER BY sum(Delegates) DESC) AS Rank,\
            Candidate_name,\
            IFNULL(COUNT(Delegates), 0) AS Total_States,\
            IFNULL(sum(Delegates), 0) AS Total_Delegates\
    FROM State_lead\
    WHERE Polling_rank = 1 \
    GROUP BY Candidate_name \
    ORDER BY Rank "

    # Execute Query
    result = db.engine.execute(query)

    # Create empty list
    delegate_lead = []

    # Iterate rows and append relative column values to a dictionary
    for row in result:
        name = {}
        name["Rank"] = row[0]
        name["Candidate_Name"] = row[1]
        name["Total_Leading_states"] = row[2]
        name["Total_Leading_Delegates"] = row[3]
        delegate_lead.append(name)          # Append this dictionary to list

    return render_template('q3.html',delegate_rank=delegate_lead)
################################# QUERY 3 ####################################


################################# QUERY 4 ####################################
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
    topNpf_rank = " LIMIT 0, %s" % topNpf
    query += topNpf_rank


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
################################# QUERY 4 ####################################


################################# QUERY 5 ####################################
@app.route("/q5", methods=["POST", "GET"])
def Query_5():

    canName = request.args.get('canName')

    print(canName)
    # Query
    query = "SELECT DISTINCT(CONCAT(CANDIDATE.First_name,' ',CANDIDATE.Last_name)) AS Candidate_Name,\
    State.State_name,Polling.Polling_percent,Polling.Check_date\
    FROM CANDIDATE,State,Polling\
    WHERE CANDIDATE.State_id = Polling.State_id AND CANDIDATE.Candidate_id = Polling.Candidate_id AND CANDIDATE.State_id = State.State_id"

    query += " AND "
    query += "CONCAT(CANDIDATE.First_name,' ',CANDIDATE.Last_name) = '%s' " % canName
    query += "  ORDER BY Check_date"

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
        name["Check_date"] = row[3]
        candidate_names.append(name)          # Append this dictionary to list

    return render_template('q5.html',can_in_home=candidate_names,canName=canName)
################################# QUERY 5 ####################################


################################# QUERY 6 ####################################

@app.route("/q6", methods=["POST", "GET"])
def Query_6():
    #Query
    query = "\
    WITH Ads_by_date AS (\
    SELECT Ad_id,\
           Platform_name,\
           State_name,\
           Ad_title,\
           Advertisement.State_id,\
           Affiliates.Candidate_id,\
           CONCAT(First_name, ' ', Last_name) as Candidate_Name,\
           Created_time as Ad_Start_Date,\
           End_time as Ad_End_Date,\
           Cost\
    FROM Advertisement\
    LEFT JOIN Affiliates ON Affiliates.Affiliate_id = Advertisement.Group_id\
    LEFT JOIN State ON State.State_id = Advertisement.State_id\
    LEFT JOIN Ad_platform using(Platform_id)\
    LEFT JOIN CANDIDATE on CANDIDATE.Candidate_id = Affiliates.Candidate_id\
    ),\
    Ad_Start_Poll AS (\
    SELECT Ad_id,\
           Advertisement.Created_time AS Ad_Start_Time,\
           Check_date AS Poll_Check_Date,\
           Polling_percent AS Ad_Start_Poll\
    FROM Polling, Advertisement, Affiliates\
    WHERE Polling.Candidate_id = Affiliates.Candidate_id AND\
        Polling.State_id = Advertisement.State_id AND\
        Group_id = Affiliate_id AND Check_date < Created_time\
    ORDER BY Polling.Candidate_id, Polling.State_id\
    ),\
    Ad_End_Poll AS (\
    SELECT Ad_id,\
       Advertisement.End_time AS Ad_End_Time,\
       Check_date AS Poll_Check_Date,\
       Polling_percent AS Ad_End_Poll\
    FROM Polling, Advertisement, Affiliates\
    WHERE Polling.Candidate_id = Affiliates.Candidate_id AND\
        Polling.State_id = Advertisement.State_id AND Group_id = Affiliate_id AND Check_date > End_time\
    ORDER BY Polling.Candidate_id, Polling.State_id\
    )\
    SELECT Candidate_Name,\
           Ad_title,\
           Platform_name,\
           State_name,\
           Ad_Start_Date,\
           Ad_End_Date,\
           (Ad_End_Poll - Ad_Start_Poll) AS Poll_Difference,\
           Cost\
    FROM Ads_by_date\
    LEFT JOIN Ad_Start_Poll USING (Ad_id)\
    LEFT JOIN Ad_End_Poll USING (Ad_id)\
    WHERE (Ad_End_Poll - Ad_Start_Poll) IS NOT NULL\
    ORDER BY Candidate_Name "

    # Execute Query
    result = db.engine.execute(query)

    # Create empty list
    Ad_spending_worth = []

    # Iterate rows and append relative column values to a dictionary
    for row in result:
        name = {}
        name["Candidate_name"] = row[0]
        name["Ad_title"] = row[1]
        name["Platform_name"] = row[2]
        name["State_name"] = row[3]
        name["Ad_Start_Date"] = row[4]
        name["Ad_End_Date"] = row[5]
        name["Poll_diff"] = row[6]
        name["Ad_cost"] = row[7]
        Ad_spending_worth.append(name)          # Append this dictionary to list

    return render_template('q6.html',Ad_spending_worth=Ad_spending_worth)
################################# QUERY 6 ####################################


################################# QUERY 7 ####################################
@app.route("/q7", methods=["POST", "GET"])
def Query_7():

    #canNameaf = request.args.get('canNameaf')
    aflist = request.form.getlist('aflist')
    i = 1

    
    # Query
    query = "SELECT DISTINCT(Affiliates.Affiliate_name),(CONCAT(CANDIDATE.First_name,' ',CANDIDATE.Last_name)) AS Candidate_Name\
    FROM CANDIDATE, Affiliates\
    WHERE CANDIDATE.Candidate_id = Affiliates.Candidate_id"

    
    if len(aflist) == 1:
        canNameaf = request.form.get('aflist')
        query += " AND "
        query += "CONCAT(CANDIDATE.First_name,' ',CANDIDATE.Last_name) = '%s' " % canNameaf

    elif len(aflist) > 1:
        query += " AND ("
        
        for item in aflist:
            if i < len(aflist):
                query += "CONCAT(CANDIDATE.First_name,' ',CANDIDATE.Last_name) = '%s' " % item
                query += "OR "
                i += 1
            
            else:
                query += "CONCAT(CANDIDATE.First_name,' ',CANDIDATE.Last_name) = '%s') " % item
    
        query += " ORDER BY Candidate_Name"

    # Show poll data of only user specified candidate


    # Execute Query
    result = db.engine.execute(query)

    # Create empty list
    candidateaf_names = []

    # Iterate rows and append relative column values to a dictionary
    for row in result:
        name = {}
        name["Affiliate_name"] = row[0]
        name["Candidate_Name"] = row[1]    
        candidateaf_names.append(name)          # Append this dictionary to list

    return render_template('q7.html',af_name=candidateaf_names, aflist=aflist) #,canNameaf=canNameaf)
################################# QUERY 7 ####################################


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
