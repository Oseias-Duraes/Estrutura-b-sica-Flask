from flask import *

app = Flask(__name__)

@app.route ("/")
def hello ():
    return 'Olá mundo'

app.run()