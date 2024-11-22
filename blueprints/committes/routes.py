from flask import Blueprint, render_template, request
from .committes_db import get_nagar_committes, get_campus_committes, get_mavi_committes

committes = Blueprint('committes',__name__, template_folder="templates")



@committes.route('/committes')
def index():
    nagar_commites = get_nagar_committes()
    campus_commites = get_campus_committes()
    mavi_commites = get_mavi_committes()
    return render_template(
        "committes.html",
        nagar_committes = (nagar_commites, len(nagar_commites)),
        campus_committes = (campus_commites, len(campus_commites)),
        mavi_committes = (mavi_commites, len(mavi_commites))
        )

@committes.route('/committes/view')
def view_committes():
    name = request.args.get('committe_id', 'Guest')
    return render_template('view-committe.html', name=name)