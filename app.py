from flask import Flask, jsonify, request
import requests

from database import Database

app = Flask(__name__)


@app.get("/greet")
def index():
    return "Hello!"


@app.get("/element")
def element():
    element_symbol = request.args.get("symbol")
    db = Database()

    response = jsonify(db.get_element_by_symbol(element_symbol))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response






