from flask import Flask, request
import app, helper

app = Flask(__name__)

ASSET_DIR = "" # where repo data will be stored
ADMIN_PASSWD = "1234" # get from environment variable

@app.route("/", methods=["GET", "POST"]) # loads homepage
def main():
	if request.method == "POST":
		message = request.form["message"]
		res = app.classify(message)
		return helper.load_file("result.html")
	return helper.load_file("index.html")



if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8001, debug=True)
