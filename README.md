# API Quiz - Tests des routes ✅

Ce README fournit des commandes `curl` pour tester toutes les routes exposées par l'application Flask.

> Prérequis
> - Depuis la racine du projet :
>   ```bash
>   export FLASK_APP=todo.app
>   flask run
>   ```
> - Base URL utilisée dans les exemples : `http://127.0.0.1:5000`

---

## 1) Récupérer tous les questionnaires 📋
- Route : GET /api/questionnaires

```
curl -i http://127.0.0.1:5000/api/questionnaires
```

---

## 2) Récupérer un questionnaire par id 🔎
- Route : GET /api/questionnaires/:id

```
curl -i http://127.0.0.1:5000/api/questionnaires/1
```

---

## 3) Créer un questionnaire ➕
- Route : POST /api/questionnaires

```
curl -i -H "Content-Type: application/json" -X POST -d '{"nom":"Mon Questionnaire"}' http://127.0.0.1:5000/api/questionnaires
```

---

## 4) Mettre à jour un questionnaire ✏️
- Route : PUT /api/questionnaires/:id

```
curl -i -H "Content-Type: application/json" -X PUT -d '{"nom":"Nouveau nom"}' http://127.0.0.1:5000/api/questionnaires/1
```

---

## 5) Supprimer un questionnaire ❌
- Route : DELETE /api/questionnaires/:id

```
curl -i -X DELETE http://127.0.0.1:5000/api/questionnaires/1
```

---

## 6) Récupérer toutes les questions (tous questionnaires) 🧾
- Route : GET /api/questions

```
curl -i http://127.0.0.1:5000/api/questions
```

---

## 7) Récupérer les questions d'un questionnaire ✅
- Route : GET /api/questionnaires/:questionnaire_id/questions

```
curl -i http://127.0.0.1:5000/api/questionnaires/1/questions
```

---

## 8) Créer une question (ouverte) 📝
- Route : POST /api/questionnaires/:questionnaire_id/questions

```
curl -i -H "Content-Type: application/json" -X POST -d '{"numero":1,"texte":"Quelle est la capitale de la France ?","reponse":"Paris"}' http://127.0.0.1:5000/api/questionnaires/1/questions
```

---

## 9) Créer une question (fermée) ✅ / ❌
- Route : POST /api/questionnaires/:questionnaire_id/questions

```
curl -i -H "Content-Type: application/json" -X POST -d '{"numero":2,"texte":"Combien d\'états aux USA ?","proposition1":"50","proposition2":"48","bonne_reponse":1}' http://127.0.0.1:5000/api/questionnaires/1/questions
```

---

## 10) Supprimer une question d'un questionnaire 🗑️
- Route : DELETE /api/questionnaires/:questionnaire_id/questions/:question_id

```
curl -i -X DELETE http://127.0.0.1:5000/api/questionnaires/1/questions/1
```

---

Notes & conseils:
- Pour les requêtes POST et PUT, le serveur renvoie `400` si les champs obligatoires manquent.
- Si vous modifiez les modèles, relancez `flask syncdb` (ou supprimez `quiz.db`) pour appliquer le schéma mis à jour.

---

Bonne exploration ! 💡
