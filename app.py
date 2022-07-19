from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
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