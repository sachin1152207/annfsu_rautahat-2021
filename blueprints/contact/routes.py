from flask import Blueprint, render_template

contact = Blueprint('contact', __name__, template_folder="templates")

@contact.route('/contact')
def index():
    return render_template('contact.html')