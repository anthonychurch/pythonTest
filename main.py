from flask import Flask
app = Flask(__name__)

from people import employee
e = employee.Employee()

@app.route('/')
def hello_world():
  
  return 'Hello, World!'

if __name__ == '__main__':
  app.run()
