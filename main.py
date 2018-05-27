from flask import Flask
app = Flask(__name__)

#"""
#Import a class from a subfolder and instantiating the class.
#"""
from people import employee.
#e = employee.Employee()

#"""
#@app.route('/') is a decorator.
#In this case the @app.route('/') decorator is calling the app.route('/')(index)().
#"""
@app.route('/')
def home():
  return 'stuff'

if __name__ == '__main__':
  app.run(debug=True)
