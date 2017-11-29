import os, sqlite3
from flask import Flask, request, render_template
# https://code-maven.com/using-templates-in-flask
# https://www.tutorialspoint.com/python/python_database_access.htm
# http://flask.pocoo.org/docs/0.12/quickstart/
# http://flask.pocoo.org/docs/0.12/tutorial/introduction/
app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('home.html')

@app.route('/mehedi')
def mehedi():
  return 'Mehedi'

if __name__ == '__main__':
  app.run(debug=True)