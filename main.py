from flask import Flask
app = Flask(__name__)

import test

@app.route('/')
def hello_world():
  t = test.test()
  return 'Hello, World!'

if __name__ == '__main__':
  app.run()
