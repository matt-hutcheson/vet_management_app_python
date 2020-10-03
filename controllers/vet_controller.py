from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.src.vet import Vet

import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)

# INDEX
@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", all_vets = vets)