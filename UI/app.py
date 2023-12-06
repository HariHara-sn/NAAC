'''from flask import Flask,render_template,request,url_for,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)
app.secret_key ='pri'

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="kGISL"
app.config["MYSQL_DB"]="kiteissue"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
conn=MySQL(app)

@app.route('/',methods = ['GET','POST'])
def login():
   if request.method =='POST':
      username=request.form['username']
      password=request.form['password']
      
      con=conn.connection.cursor()
      sql="insert into login(username,password) values(%s,%s)"
      con.execute(sql,(username,password))
      con.connection.commit()
      con.close()
      return render_template('home.html')
   return render_template('login.html')

# @app.route('/homepage')
# def homepage():
#    if request.method =='POST':

#       return render_template('home.html')
#    return render_template('login.html')


@app.route('/home')
def home():
   return render_template('home.html')
@app.route('/hostel_issue_form')
def hostel_issue_form():
   return render_template('hostel_issue_form.html')

# @app.route('/hostel_issue')
# def hostel_issuee():
#    if request.method =='POST':

#       return render_template(redirect (url_for('hostel_issue_form.html')))
#    return render_template('home.html')

@app.route('/hostel_issue_form',methods = ['GET','POST'])
def hostelissue():
   if request.method =='POST':
      name=request.form['firstName']
      email=request.form['email']
      room=request.form['room']
      cot=request.form['cot']
      natureOfComplaint=request.form['complaintNature']
      quality=request.form['qualityOfFood']
      description=request.form['detailsOfComplaint']
      
      con=conn.connection.cursor()
      sql="insert into hostelissue(name,email,room,cot,natureOfComplaint,quality,description) values(%s,%s,%s,%s,%s,%d,%s)"
      con.execute(sql, (name,email,room,cot,natureOfComplaint,quality,description) )
      con.connection.commit()
      con.close()
      return render_template('success_msg_hostel.html')
   return render_template('hostel_issue_form.html')

@app.route('/success_msg_hostel')
def success_msg_hostel():
   return render_template('success_msg_hostel.html')
   






if __name__=='__main__':
    app.run(debug=True)'''