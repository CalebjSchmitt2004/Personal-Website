from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("homepage.html")


@views.route("/services")
def services():
    return render_template("services.html")


@views.route("/projects")
def projects():
    return render_template("projects.html")


@views.route("/about")
def about():
    return render_template("about.html")