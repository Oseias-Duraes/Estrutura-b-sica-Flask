from flask import *

app = Flask(__name__)

@app.route ("/")
def hello ():
    return render_template ("homepage.html")

@app.route ('/financeiro')
def financeiro():
    return render_template ("financeiro.html")
app.run(debug = True)
