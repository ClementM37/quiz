import json
from .app import db


class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(128), nullable=False)
    questions = db.relationship('Question', backref='questionnaire', cascade='all, delete-orphan', lazy=True)

    def to_json(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'questions': [q.to_json() for q in self.questions]
        }


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texte = db.Column(db.Text, nullable=False)
    reponses = db.Column(db.Text, nullable=False)  # stored as JSON string
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'), nullable=False)

    def to_json(self):
        try:
            reponses = json.loads(self.reponses)
        except Exception:
            reponses = []
        return {
            'id': self.id,
            'texte': self.texte,
            'reponses': reponses,
            'questionnaire_id': self.questionnaire_id
        }


def get_all_questionnaires():
    return Questionnaire.query.all()


def get_questionnaire_by_id(id):
    return Questionnaire.query.get(id)


def create_questionnaire(nom):
    q = Questionnaire(nom=nom)
    db.session.add(q)
    db.session.commit()
    return q


def delete_questionnaire_by_id(id):
    q = get_questionnaire_by_id(id)
    if q:
        db.session.delete(q)
        db.session.commit()
        return True
    return False


def get_all_questions():
    return Question.query.all()