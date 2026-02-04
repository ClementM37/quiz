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
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    texte = db.Column(db.Text, nullable=False)
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'), nullable=False)
    type = db.Column(db.String(50))

    __mapper_args__ = {'polymorphic_identity': 'base', 'polymorphic_on': type}

    def to_json(self):
        return {
            'id': self.id,
            'numero': self.numero,
            'texte': self.texte,
            'questionnaire_id': self.questionnaire_id,
            'type': self.__class__.__name__
        }

class QuestionOuverte(Question):
    __mapper_args__ = {'polymorphic_identity': 'ouverte'}
    reponse = db.Column(db.Text, nullable=True)

    def to_json(self):
        data = super().to_json()
        data['reponse'] = self.reponse
        return data

class QuestionFermee(Question):
    __mapper_args__ = {'polymorphic_identity': 'fermee'}
    proposition1 = db.Column(db.Text, nullable=True)
    proposition2 = db.Column(db.Text, nullable=True)
    bonne_reponse = db.Column(db.Integer, nullable=True)

    def to_json(self):
        data = super().to_json()
        data['proposition1'] = self.proposition1
        data['proposition2'] = self.proposition2
        data['bonne_reponse'] = self.bonne_reponse
        return data

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

def add_open_question(numero, texte, reponse, questionnaire_id):
    q = QuestionOuverte(numero=numero, texte=texte, reponse=reponse, questionnaire_id=questionnaire_id)
    db.session.add(q)
    return q

def add_closed_question(numero, texte, proposition1, proposition2, bonne_reponse, questionnaire_id):
    q = QuestionFermee(numero=numero, texte=texte, proposition1=proposition1, proposition2=proposition2, bonne_reponse=bonne_reponse, questionnaire_id=questionnaire_id)
    db.session.add(q)
    return q

def create_sample_questionnaire(nom, questions=None):
    q = create_questionnaire(nom)
    if questions:
        for ques in questions:
            if ques.get('type') == 'ouverte':
                add_open_question(ques['numero'], ques['texte'], ques['reponse'], q.id)
            elif ques.get('type') == 'fermee':
                add_closed_question(ques['numero'], ques['texte'], ques['proposition1'], ques['proposition2'], ques['bonne_reponse'], q.id)
    return q