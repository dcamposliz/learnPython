from flask import Flask # imports a Flask class
app = Flask(__name__) # creates an instance of thtis class

@app.route('/') # sets what URL should trigger our function
def hello_world(): # returns message
    return 'Hello, World!'
