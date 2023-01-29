from flask import Blueprint, jsonify, request
from models.models import User
from models import db
from markupsafe import escape


usr = Blueprint('usr', __name__)


@usr.route('/',methods=['GET'])
def get_users():
    users=User.query.all()
    if users:
        return jsonify([u.to_dict() for u in users]),200
    return jsonify({'error': 'User not found'}), 204

@usr.route('/id/<ID>',methods=['GET'])
def get_user_by_id(ID):
    user=User.query.filter_by(id=escape(ID)).first()
    if user:
        return jsonify(user.to_dict()),200
    return jsonify({'error': 'User not found'}), 204

@usr.route('/email',methods=['GET'])
def get_user_by_email():
    email=request.headers.get('email')
    user=User.query.filter_by(email=escape(email)).first()
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found'}), 204

@usr.route('/trener_id/<trener_id>',methods=['GET'])
def get_user_by_trener_id(trener_id):
    user=User.query.filter_by(trener_id=escape(trener_id))
    if user:
        return jsonify([u.to_dict() for u in user]), 200
    return jsonify({'error': 'Users not found'}), 204

@usr.route('/surname/<surname>',methods=['GET'])
def get_user_by_surname(surname):
    user=User.query.filter_by(surname=escape(surname))
    if user:
        return jsonify([u.to_dict() for u in user]), 200
    return jsonify({'error': 'User not found'}), 204


@usr.route('/',methods=['POST'])
def add_user():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.json
        user = User(name=data["name"],surname=data["surname"],
                email=data["email"],password=data["password"])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201
    return 'Content-Type not supported!', 400

@usr.route('/<ID>',methods=['PUT'])
def update_user_data(ID):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data=request.json
        user = User.query.filter_by(id=escape(ID)).first()
        if user:
            user.name=data["name"]
            user.surname=data["surname"]
            user.email=data["email"]
            user.trener_id=data["trener_id"]
            user.password =data["passowrd"]
            db.session.commit()
            return jsonify(user.to_dict()), 200
        return jsonify({'error': 'User not found'}), 204
    return 'Content-Type not supported!', 400

@usr.route('/<ID>',methods=['DELETE'])
def delete_trener(ID):
    User.query.filter_by(id=ID).delete()
    db.session.commit()
    return jsonify({'error':'ok'}),200
