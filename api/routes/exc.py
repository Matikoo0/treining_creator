from flask import Blueprint, jsonify, request
from models.models import Exercise
from models import db
from markupsafe import escape


exc = Blueprint('exc', __name__)


@exc.route('/', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    if exercises:
        return jsonify([exercise.to_dict() for exercise in exercises]), 200
    return jsonify({'error': 'Exercise not found'}), 204

@exc.route('/id/<ID>',methods=['GET'])
def get_exercise_by_id(ID):
    exc=Exercise.query.filter_by(id=escape(ID)).first()
    if exc:
        return jsonify(exc.to_dict()),200
    return jsonify({'error': 'Exercise not found'}), 204


@exc.route('/name/<name>', methods=['GET'])
def get_exercises_by_name(name):
    exercises = Exercise.query.filter_by(name=escape(name))
    if exercises:
        return jsonify([exercise.to_dict() for exercise in exercises]), 200
    return jsonify({'error': 'Exercise not found'}), 204


@exc.route('/trener_id/<trener_id>', methods=['GET'])
def get_exercises_by_treiner_id(trener_id):
    exercises = Exercise.query.filter_by(id=escape(trener_id))
    if exercises:
        return jsonify([exc.to_dict() for exc in exercises]), 200
    return jsonify({'error': 'Exercise not found'}), 204


@exc.route('/trener_id_and_name/<trener_id>/<name>', methods=['GET'])
def get_exercise_by_trener_id_and_name(name, trener_id):
    exercises = Exercise.query.filter_by(name=escape(name), trener_id=escape(trener_id))
    if exercises:
        return jsonify([exercise.to_dict() for exercise in exercises]), 200
    return jsonify({'error': 'Exercise not found'}), 204


@exc.route('/', methods=['POST'])
def add_exercise():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.json
        exercise = Exercise(name=data["name"], url=data["url"], zaang=data["zaang"], trener_id=data["trener_id"])
        db.session.add(exercise)
        db.session.commit()
        return jsonify(exercise.to_dict()), 201
    return 'Content-Type not supported!', 400


@exc.route('/<ID>', methods=['PUT'])
def update_exercise_data(ID):
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        exc = Exercise.query.filter_by(id=ID).first()
        data = request.json
        if exc:
            exc.name = data["name"]
            exc.url = data["url"]
            exc.zaang = data["zaang"]
            exc.trener_id = data["trener_id"]
            db.session.commit()
            return jsonify(exc.to_dict()), 200
        return jsonify({'error': 'Exercise not found'}), 204
    return 'Content-Type not supported!', 400


@exc.route('/<ID>', methods=['DELETE'])
def delete_exercise(ID):
    Exercise.query.filter_by(id = ID).delete()
    db.session.commit()
    return jsonify({'error':'ok'}),200