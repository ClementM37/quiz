from flask import jsonify, abort, request
from .app import app, db
from flask import url_for
from .models import *

def make_public_questionnaire(q):
    new = {}
    for field in q:
        if field == 'id':
            new['uri'] = url_for('get_questionnaire', id=q['id'], _external=True)
        else:
            new[field] = q[field]
    return new

@app.route('/api/questionnaires', methods=['GET'])
def get_questionnaires():
    all_q = get_all_questionnaires()
    return jsonify([make_public_questionnaire(q.to_json()) for q in all_q])

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

@app.route('/api/questions', methods=['GET'])
def get_all_questions_route():
    all_questions = get_all_questions()
    return jsonify([q.to_json() for q in all_questions])

@app.route('/api/questionnaires/<int:questionnaire_id>/questions', methods=['GET'])
def get_questions(questionnaire_id):
    q = get_questionnaire_by_id(questionnaire_id)
    if q is None:
        abort(404)
    return jsonify([q.to_json() for q in q.questions])

@app.route('/api/questionnaires/<int:questionnaire_id>/questions', methods=['POST'])
def create_question(questionnaire_id):
    q = get_questionnaire_by_id(questionnaire_id)
    if q is None:
        abort(404)
    
    data = request.json
    if not data or 'numero' not in data or 'texte' not in data:
        abort(400)
    
    if 'reponse' in data:
        question = QuestionOuverte(
            numero=data['numero'],
            texte=data['texte'],
            reponse=data['reponse'],
            questionnaire_id=questionnaire_id
        )
    elif all(k in data for k in ['proposition1', 'proposition2', 'bonne_reponse']):
        question = QuestionFermee(
            numero=data['numero'],
            texte=data['texte'],
            proposition1=data['proposition1'],
            proposition2=data['proposition2'],
            bonne_reponse=data['bonne_reponse'],
            questionnaire_id=questionnaire_id
        )
    else:
        abort(400)
    
    db.session.add(question)
    db.session.commit()
    return jsonify(question.to_json()), 201

@app.route('/api/questionnaires/<int:questionnaire_id>/questions/<int:question_id>', methods=['PUT'])
def update_question(questionnaire_id, question_id):
    question = Question.query.filter_by(id=question_id, questionnaire_id=questionnaire_id).first()
    if question is None:
        abort(404)
    
    data = request.json
    if not data:
        abort(400)

    if 'numero' in data: question.numero = data['numero']
    if 'texte' in data: question.texte = data['texte']

    if question.type == 'ouverte' and 'reponse' in data:
        question.reponse = data['reponse']
    elif question.type == 'fermee':
        if 'proposition1' in data: question.proposition1 = data['proposition1']
        if 'proposition2' in data: question.proposition2 = data['proposition2']
        if 'bonne_reponse' in data: question.bonne_reponse = data['bonne_reponse']

    db.session.commit()
    return jsonify(question.to_json())

@app.route('/api/questionnaires/<int:questionnaire_id>/questions/<int:question_id>', methods=['DELETE'])
def delete_question(questionnaire_id, question_id):
    question = Question.query.filter_by(id=question_id, questionnaire_id=questionnaire_id).first()
    if question is None:
        abort(404)
    db.session.delete(question)
    db.session.commit()
    return '', 204