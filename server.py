#header
from flask import Flask, render_template, request, redirect, Response
from file_handler import get_file
app = Flask(__name__)
#header

@app.route("/")
def welcome():
	content = get_file("http/index.html")
	return Response(content, mimetype ="text/html")
@app.route("/test")
def default_api():
	return("Health-status: ok")


#footer
if __name__ == "__main__":
    app.run(debug=True)
#footer