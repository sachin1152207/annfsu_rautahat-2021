from flask import Blueprint, render_template

blogs = Blueprint('blogs',__name__, template_folder="templates")

@blogs.route('/blogs')
def index():
    return render_template("blogs.html")