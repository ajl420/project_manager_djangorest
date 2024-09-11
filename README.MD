## GESTION DE PROJET
### Lancement local
Modifier le fichier .env est changer les valeur selon la configuration de votre base de donnees:

```
DB_USER=AJL420 
DB_PASSWORD=comme  
DB_NAME=project_man  
DB_HOST=localhost  
DB_PORT=5432  
```
Installer les dependances:
```shell
python -m pip install -r requirement
```

Lancer maintenant le migration pour synchroniser avec votre base de donnees:
```shell
python manage.py migrate
```

Creer un compte admin pour acceder a l'interface admin:
```shell
python manage.py createsuperuser
```

Lancer le test pour verifier que tous fonctionnent:
```shell
python manage.py test
```

Lancer le serveur pour le deployement en mode developpement:
```shell
python manage.py runserver [hote:port]
```

### Lancement dans docker
Lancer tout d'abord le service de base de donnees et attent quelques secondes:
```shell
docker-compose up db -d
```
Puis lancer le service web:
```shell
docker-compose up web -d
```
Fait maintenat la migration de votre base de donnees
```shell
docker-compose exec web python manage.py migrate
```

Creer un compte admin pour acceder a l'interface admin:
```shell
docker-compose exec web python manage.py createsuperuser
```
### Lien
admin: [http://locahost:8000/admin](http://locahost:8000/admin)<br>
api: [http://locahost:8000/api](http://locahost:8000/api)<br>
docs: [http://locahost:8000/docs](http://locahost:8000/docs)


