from flask import Flask, render_template, request, rediret
from flask import Blueprint

from models.src.client import Client

import repositories.client_repository as client_repository

clients_blueprint = Blueprint("clients", __name__)

# INDEX
@clients_blueprint.route("/clients")
def clients():
    clients = client_repository.select_all()