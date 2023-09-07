import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session, abort
from flask_session import Session
from flask_mail import Mail, Message
from tempfile import mkdtemp
from config import mail_username, mail_password

# Configure application
app = Flask(__name__)

@app.after_request
def add_cache_control(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


# Custom filter

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config["MAIL_SERVER"] = "smtp-mail.outlook.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = mail_username
app.config["MAIL_PASSWORD"] = mail_password
##app.config["MAIL_DEFAULT_SENDER"] = os.environ["MAIL_DEFAULT_SENDER"]
##app.config["MAIL_SQLALCHEMY_DATABASE_URI"] = "mysql+"
# Configure CS50 Library to use SQLite database
mail = Mail(app)
db = SQL("sqlite:///project1.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
   raise RuntimeError("API_KEY not set")


@app.route("/") ##method=["GET", "POST"]
def index():
   return render_template("index.html")


@app.route("/contact.html", methods=['GET', 'POST'])
def contact():
     if request.method == "POST":
        name = request.form.get('name')
        lname = request.form.get('lname')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message(subject=f"Mail from {name}", body=f"Name: {name}\nE-Mail: {email}\nlname: {lname}\n\n\n{message}", sender=mail_username, recipients=['mahsa.ah2018@gmail.com'])
        mail.send(msg)
        return render_template("contact.html", success=True)

     return render_template("contact.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/teacher.html")
def single():
    return render_template("teacher.html")

@app.route("/homa.html")
def homa():
    return render_template("homa.html")

@app.route("/mehrsa.html")
def mehrsa():
    return render_template("mehrsa.html")

if __name__ == '__main__':
    app.run()

