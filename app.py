from flask import Flask
from flask import render_template

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
    totaaltekst = ""
    totaaltekst += geefBovenTekst()
    totaaltekst += geefTussenTekst(myresult)
    totaaltekst += geefEindTekst()
    return totaaltekst


@app.route("/koopmeubel/<idvanmeubel>")
def tweedefunctie(idvanmeubel):
    mycursor.execute("SELECT * FROM meubel WHERE id = "+str(idvanmeubel)+" ;")
    myresult = mycursor.fetchone()
    return render_template('kooppagina.html', meubel=myresult)



@app.route("/voorbeeldtemplate")
def meteentemplate():
    mycursor.execute("SELECT * FROM meubel")
    myresult = mycursor.fetchall()
    return render_template('voorbeeld.html', naam="doen", users=myresult)












def geefBovenTekst():
    return """
<style>
h3{
    color:orange;
}    
</style>
<script>
    function daargaanwe(idmeubel){
        window.location = "http://localhost:5000/koopmeubel/"+idmeubel
    }
</script>
<div>
    <h1>Dit zijn onze meubels</h1>
</div>
    """

def geefTussenTekst(recordset):
    tempTekst = ""
    for x in recordset:
        #print(x[1])
        tempTekst += "<div><h3>"
        tempTekst += x[2]
        tempTekst += "</h3><img src="
        tempTekst += x[1]
        tempTekst += " width=180px></div><button onclick=daargaanwe("
        tempTekst += str(x[0])
        tempTekst += ")>koopmij</button>"
    return tempTekst

def geefEindTekst():
    return """
<div>
    <hr>
</div>
    """
