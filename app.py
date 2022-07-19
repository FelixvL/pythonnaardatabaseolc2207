from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    detekst = """
<div>
    <h1>Tafel</h1>
    <img src="tafel.jpg">

</div>
"""
    return detekst