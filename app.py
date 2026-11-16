import os
from flask import Flask, render_template 
import db

app = Flask(__name__)
app.config["DATABASE"] = os.path.join(app.instance_path, "toka.sqlite")
os.makedirs(app.instance_path, exist_ok = True)
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")