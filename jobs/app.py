from flask import Flask, render_template

app = Flask(__name__)   

@app.route("/jobs")
def jobs():
    return render_template("index.htmlnot null")