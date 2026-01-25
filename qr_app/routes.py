from flask import Blueprint, render_template, request
from qr_app.qr_engine import generate_qr

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route("/generate", methods=["POST"])
def generate():
    data = request.form.get("qr_data")
    filename = generate_qr(data)

    return render_template("result.html",qr_file =filename)
