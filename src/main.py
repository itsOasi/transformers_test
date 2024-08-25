from flask import Flask, request, render_template
import app, helper

flask_app = Flask(__name__)

ASSET_DIR = "" # where repo data will be stored
ADMIN_PASSWD = "1234" # get from environment variable

@flask_app.route("/", methods=["GET", "POST"]) # loads homepage
def main():
	if request.method == "POST":
		message = request.form["prompt"]
		res = app.get_generated(message)
		return render_template("result.html", result=res)
	return render_template("index.html")

flask_app.route("analyze", methods=["POST"])
def analyze():
	message = request.form["prompt"]
	res = app.get_sentiment(message)
	return render_template("result.html", result=res)

flask_app.route("generate", methods=["POST"])
def generate():
	message = request.form["prompt"]
	res = app.get_generated(message)
	return render_template("result.html", result=res)

flask_app.route("answer", methods=["POST"])
def sentiment():
	message = request.form["prompt"]
	res = app.get_sentiment(message)
	return render_template("result.html", result=res)


if __name__ == "__main__":
	flask_app.run(host="0.0.0.0", port=8000, debug=True)
