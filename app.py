from flask import Flask, render_template

from controllers.vet_controller import vets_blueprint
from controllers.client_controller import clients_blueprint
# from controllers.patient_controller import patients_blueprint
# from controllers.treatment_controller import treatments_blueprint

app = Flask(__name__)

app.register_blueprint(clients_blueprint)
# app.register_blueprint(patients_blueprint)
# app.register_blueprint(treatments_blueprint)
app.register_blueprint(vets_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)