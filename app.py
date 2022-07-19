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
    boventekst = """
<style>
h3{
    color:orange;
}    
</style>
<div>
    <h1>Dit zijn onze meubels</h1>
</div>
    """
    tussentekst = ""
    for x in myresult:
        #print(x[1])
        tussentekst += "<div><h3>"
        tussentekst += x[2]
        tussentekst += "</h3><img src="
        tussentekst += x[1]
        tussentekst += " width=150px></div>"
    ondertekst = """
<div>
    <hr>
</div>
    """

    detekst = """


<div>
    <h3>Stoel</h3>
    <img src="stoel.jpg" width="150px">

</div>
"""
    return boventekst + tussentekst + ondertekst


#    SELECT * FROM meubel