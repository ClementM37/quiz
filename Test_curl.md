# Tests des routes API Quiz
# Lancer d'abord : flask syncdb
# Puis : flask run

# 1) Liste des questionnaires
curl -i http://127.0.0.1:5000/api/questionnaires

# 2) Questionnaire par ID
curl -i http://127.0.0.1:5000/api/questionnaires/1

# 3) Créer un questionnaire
curl -i -H "Content-Type: application/json" -X POST -d '{"nom":"Culture Générale"}' http://127.0.0.1:5000/api/questionnaires

# 4) Modifier un questionnaire
curl -i -H "Content-Type: application/json" -X PUT -d '{"nom":"Nouveau Titre"}' http://127.0.0.1:5000/api/questionnaires/1

# 5) Supprimer un questionnaire
curl -i -X DELETE http://127.0.0.1:5000/api/questionnaires/1

# 6) Liste globale des questions
curl -i http://127.0.0.1:5000/api/questions

# 7) Questions d'un questionnaire
curl -i http://127.0.0.1:5000/api/questionnaires/1/questions

# 8) Ajouter une question ouverte
curl -i -H "Content-Type: application/json" -X POST -d '{"numero":1,"texte":"Quelle est la capitale de la France ?","reponse":"Paris"}' http://127.0.0.1:5000/api/questionnaires/1/questions

# 9) Ajouter une question fermée
```
curl -i -H "Content-Type: application/json" -X POST -d '{"numero":2,"texte":"Combien d'\''états aux USA ?","proposition1":"50","proposition2":"48","bonne_reponse":1}' http://127.0.0.1:5000/api/questionnaires/1/questions
```

# 10) Modifier une question ouverte
curl -i -H "Content-Type: application/json" -X PUT -d '{"texte":"Question ouverte modifiée","reponse":"Nouvelle réponse"}' http://127.0.0.1:5000/api/questionnaires/1/questions/1

# 11) Modifier une question fermée
curl -i -H "Content-Type: application/json" -X PUT -d '{"texte":"Question fermée modifiée","proposition1":"Oui","proposition2":"Non","bonne_reponse":1}' http://127.0.0.1:5000/api/questionnaires/1/questions/2

# 12) Supprimer une question
curl -i -X DELETE http://127.0.0.1:5000/api/questionnaires/1/questions/1
