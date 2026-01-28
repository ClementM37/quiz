from flask import jsonify, abort, request
from .app import app, db
from .models import (
    get_all_questionnaires,
    get_questionnaire_by_id,
    create_questionnaire,
    delete_questionnaire_by_id,
    get_all_questions,
)


@app.route('/api/questionnaires', methods=['GET'])
def get_questionnaires():
    all_q = get_all_questionnaires()
    return jsonify([q.to_json() for q in all_q])


@app.route('/api/questionnaires/<int:id>', methods=['GET'])
def get_questionnaire(id):
    q = get_questionnaire_by_id(id)
    if q is None:
        abort(404)
    return jsonify(q.to_json())


@app.route('/api/questionnaires', methods=['POST'])
def post_questionnaire():
    if not request.json or 'nom' not in request.json:
        abort(400)
    nom = request.json['nom']
    q = create_questionnaire(nom)
    return jsonify(q.to_json()), 201


@app.route('/api/questionnaires/<int:id>', methods=['PUT'])
def update_questionnaire(id):
    q = get_questionnaire_by_id(id)
    if q is None:
        abort(404)
    if not request.json or 'nom' not in request.json:
        abort(400)
    q.nom = request.json['nom']
    db.session.commit()
    return jsonify(q.to_json())


@app.route('/api/questionnaires/<int:id>', methods=['DELETE'])
def delete_questionnaire(id):
    success = delete_questionnaire_by_id(id)
    if not success:
        abort(404)
    return '', 204


@app.route('/api/questionnaires/question', methods=['GET'])
def get_questions():
    all_q = get_all_questions()
    return jsonify([q.to_json() for q in all_q])
