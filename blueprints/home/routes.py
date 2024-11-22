from flask import Blueprint, render_template
from .home_db import hero_description, get_members, get_member_word
from .utils import time_ago

home = Blueprint('home',__name__, template_folder="templates")



@home.route('/')
def index():
    return render_template(
        "index.html",
        hero_description = hero_description(),
        members = get_members(),
        members_words = get_member_word(),
        time_ago = time_ago
        )