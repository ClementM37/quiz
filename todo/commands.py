import json
from .app import app, db
from .models import *
@app.cli.command()
def syncdb():
    """Crée la base et des exemples de questionnaires/questions."""
    db.drop_all()
    db.create_all()

    q1 = create_sample_questionnaire("Questionnaire 1", questions=[
        {'type':'ouverte','numero':1,'texte':"Quelle est la capitale de la France ?", 'reponse':'Paris'},
        {'type':'fermee','numero':2,'texte':"Combien d'états aux USA ?", 'proposition1':'50','proposition2':'48','bonne_reponse':1},
    ])

    q2 = create_sample_questionnaire("Questionnaire 2", questions=[
        {'type':'fermee','numero':1,'texte':"Plus grande planète ?", 'proposition1':'Jupiter','proposition2':'Saturne','bonne_reponse':1}
    ])

    create_sample_questionnaire("Questionnaire 3")
    create_sample_questionnaire("Questionnaire 4")

    db.session.commit()
