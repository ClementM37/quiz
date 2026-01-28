from.app import app , db
from.models import create_questionnaire
@app.cli.command()
def syncdb():
    db.create_all()
    # create sample questionnaires
    q1 = create_questionnaire("Questionnaire 1")
    q2 = create_questionnaire("Questionnaire 2")
    q3 = create_questionnaire("Questionnaire 3")
    q4 = create_questionnaire("Questionnaire 4")
    db.session.add_all([q1, q2, q3, q4])
    db.session.flush()

    def add(q, texte, reponses):
        rq = Question(texte=texte, reponses=json.dumps(reponses), questionnaire_id=q.id)
        db.session.add(rq)

    add(q1, "Quelle est la capitale de la France ?", ["Paris", "Londres", "Berlin", "Madrid"])
    add(q1, "Combien detats y a-t-il aux États-Unis ?", ["50", "48", "52", "51"])
    add(q2, "Quelle est la plus grande planète du système solaire ?", ["Jupiter", "Saturne", "Terre", "Mars"])
    add(q2, "Qui a écrit 'Roméo et Juliette' ?", ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"])
    add(q3, "Quelle est la formule chimique de l'eau ?", ["H2O", "CO2", "O2", "NaCl"])
    add(q3, "Quel est le plus grand océan du monde ?", ["Océan Pacifique", "Océan Atlantique", "Océan Indien", "Océan Arctique"])
    add(q4, "Qui a peint la Joconde ?", ["Léonard de Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"])
    add(q4, "Quelle est la capitale de l'Italie ?", ["Rome", "Milan", "Naples", "Turin"])

    db.session.commit()