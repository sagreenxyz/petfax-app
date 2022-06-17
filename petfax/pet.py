from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))

bp = Blueprint('pet', __name__, url_prefix="/pets")

# pet index route
@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

# pet detail
@bp.route('/<int:id>')
def show(id):
    pet = pets[id - 1]
    return render_template('show.html', pet=pet)