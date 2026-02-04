# API Quiz — Documentation

Une API REST pour gérer des questionnaires et leurs questions (ouvertes et fermées).

## Prérequis
- Python 3.8+
- Un environnement virtuel (recommandé)
- `flask` installé (voir `requirements.txt` si fourni)


## Initialisation et lancement
- Initialiser la base de données (si l'application fournit la commande) :
```bash
flask syncdb
```
- Lancer le serveur :
```bash
flask run
```

## Opérations requises (endpoints et exemples)

1) Liste des questionnaires

```bash
curl -i http://127.0.0.1:5000/api/questionnaires
```

2) Questionnaire par ID

```bash
curl -i http://127.0.0.1:5000/api/questionnaires/1
```

3) Ajouter un questionnaire

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"nom":"Culture Générale"}' http://127.0.0.1:5000/api/questionnaires
```

4) Modifier un questionnaire

```bash
curl -i -H "Content-Type: application/json" -X PUT -d '{"nom":"Nouveau Titre"}' http://127.0.0.1:5000/api/questionnaires/1
```

5) Supprimer un questionnaire

```bash
curl -i -X DELETE http://127.0.0.1:5000/api/questionnaires/1
```

6) Liste des questions (global)

```bash
curl -i http://127.0.0.1:5000/api/questions
```

7) Questions d'un questionnaire (par ID)

```bash
curl -i http://127.0.0.1:5000/api/questionnaires/1/questions
```

8) Ajouter une question ouverte

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"numero":1,"texte":"Quelle est la capitale de la France ?","reponse":"Paris"}' http://127.0.0.1:5000/api/questionnaires/1/questions
```

9) Ajouter une question fermée

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"numero":2,"texte":"Combien d\'états aux USA ?","proposition1":"50","proposition2":"48","bonne_reponse":1}' http://127.0.0.1:5000/api/questionnaires/1/questions
```

10) Modifier une question ouverte

```bash
curl -i -H "Content-Type: application/json" -X PUT -d '{"texte":"Question ouverte modifiée","reponse":"Nouvelle réponse"}' http://127.0.0.1:5000/api/questionnaires/1/questions/1
```

11) Modifier une question fermée

```bash
curl -i -H "Content-Type: application/json" -X PUT -d '{"texte":"Question fermée modifiée","proposition1":"Oui","proposition2":"Non","bonne_reponse":1}' http://127.0.0.1:5000/api/questionnaires/1/questions/1
```

12) Supprimer une question (ouverte ou fermée)

```bash
curl -i -X DELETE http://127.0.0.1:5000/api/questionnaires/1/questions/1
```



