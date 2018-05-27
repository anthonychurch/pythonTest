from flask import Flask
app = Flask(__name__)

from people import employee
#t = test.Test()

@app.route('/')
def hello_world():
  
  return 'Hello, World!'

if __name__ == '__main__':
  app.run()
