from flask import render_template
from . import api


@api.route('/')
@api.route('/home', methods=["GET"])
def get_home():
    return render_template('home.html')


@api.route("/project", methods=["GET"])
def get_project():
    return render_template('project.html')
