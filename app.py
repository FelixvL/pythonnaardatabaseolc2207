from flask import Flask

app = Flask(__name__)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",  #port erbij indien mac
  user="root",
  password="",
  database="databasevoormeubelwinkel"
)

mycursor = mydb.cursor()


@app.route("/")
def hello_world():
    mycursor.execute("SELECT * FROM meubel")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x[1])

    detekst = """
<style>
    h3{
        color:orange;
    }    
</style>
<div>
    <h1>Dit zijn onze meubels</h1>
</div>
<div>
    <h3>Tafel</h3>
    <img src="tafel.jpg" width="150px">

</div>
<div>
    <h3>Stoel</h3>
    <img src="stoel.jpg" width="150px">

</div>
<div>
    <hr>
</div>
"""
    return detekst


#    SELECT * FROM meubel