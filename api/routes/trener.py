from flask import Blueprint, jsonify, request
from models.models import Trener
from models import db
from markupsafe import escape

from passlib.hash import pbkdf2_sha512


tre = Blueprint('tre', __name__)



@tre.route('/', methods=['GET'])
def get_treiners():
    tre = Trener.query.all()
    if tre:
        return jsonify([t.to_dict() for t in tre]), 200
    return jsonify({'error': 'Treiner not found'}), 204

@tre.route('/id/<ID>', methods=['GET'])
def get_trener_by_id(ID):
    tre = Trener.query.filter_by(id=escape(ID)).first()
    if tre:
        return jsonify(tre.to_dict()), 200
    return jsonify({'error': 'Treiner not found'}), 204


@tre.route('/email', methods=['GET'])
def get_trener_by_email():
    email=request.headers.get('email')
    tre = Trener.query.filter_by(email=escape(email)).first()
    if tre:
        return jsonify(tre.to_dict()), 200
    return jsonify({'error': 'Treiner not found'}), 204


@tre.route('/surname/<surname>', methods=['GET'])
def get_treners_by_surname(surname):
    tre = Trener.query.filter_by(surname=escape(surname))
    if tre:
        return jsonify([t.to_dict() for t in tre]), 200
    return jsonify({'error': 'Treiner not found'}), 204

@tre.route('/',methods=['POST'])
def add_trener():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.json
        trener = Trener(
        name=data["name"],surname=data["surname"],
        email=data["email"],podop=data["podop"],
        password=data["password"])
        db.session.add(trener)
        db.session.commit()
        return jsonify(trener.to_dict()), 201
    return 'Content-Type not supported!', 400

@tre.route('/<ID>',methods=['PUT'])
def update_trener_data(ID):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data=request.json
        tre = Trener.query.filter_by(id=escape(ID)).first()
        if tre:
            tre.name=data["name"]
            tre.surname=data["surname"]
            tre.email=data["email"]
            tre.podop=data["podop"]
            tre.password= data["password"]
            db.session.commit()
            return jsonify(tre.to_dict()), 200
        return jsonify({'error': 'Treiner not found'}), 204
    return 'Content-Type not supported!', 400

@tre.route('/<ID>',methods=['DELETE'])
def delete_trener(ID):
    Trener.query.filter_by(id=ID).delete()
    db.session.commit()
    return jsonify({'error':'ok'}),200

