from flask import *

app = Flask(__name__)

@app.route ("/")
def hello ():
    return 'Hello, World'

@app.route ('/financeiro')
def financeiro():
    return render_template ("financeiro.html")
app.run(debug = True)
