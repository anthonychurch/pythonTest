from flask import 


app = Flask(__name__)

@pp.route("/")
def main():
	return "Welcome!"

if __name__ == "__main__":
	app.run()