from flask import Flask, request, render_template
import app, helper

flask_app = Flask(__name__)

ASSET_DIR = "" # where repo data will be stored
ADMIN_PASSWD = "1234" # get from environment variable

@app.route("/", methods=["GET", "POST"]) # loads homepage
def main():
	if request.method == "POST":
		message = request.form["message"]
		res = app.get_sentiment(message)
		return render_template("result.html", result=res)
	return render_template("index.html")



if __name__ == "__main__":
	flask_app.run(host="0.0.0.0", port=8000, debug=True)
