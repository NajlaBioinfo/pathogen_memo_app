from flask import Blueprint, render_template
from sys import version
from flask import Flask, jsonify

#Set word_count_site_name
aboutv = Blueprint('aboutv', __name__)

@aboutv.route("/about")
def about():
    return render_template("about.html")
