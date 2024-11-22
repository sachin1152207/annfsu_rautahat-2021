from flask import Blueprint, render_template
from .about_db import get_members, about_description
about = Blueprint('about',__name__, template_folder="templates")



@about.route('/about')
def index():
    return render_template("about.html", members=get_members(), about_desc = about_description())