from flask import Flask, render_template, session, request, redirect, url_for, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "dev"
app.permanent_session_lifetime = timedelta(days=7)


@app.route("/")
def home():
    if "username" in session:
        user = session["username"]
        return render_template("index.html", username=user)
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        session["username"] = request.form["usernameField"]
        flash("Log in successful.", "info")
        return redirect(url_for("home"))
    if "username" in session:
        flash("Already log in.", "info")
        return redirect(url_for("home"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username", None)
        flash("Log out successful.", "info")
        return redirect(url_for("home"))
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
