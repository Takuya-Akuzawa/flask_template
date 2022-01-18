from flask import Blueprint, render_template


views = Blueprint('views_module', __name__, template_folder='templates')

@views.route('/')
def index():
    return render_template('index.html')