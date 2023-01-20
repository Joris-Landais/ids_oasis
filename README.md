# Projet IDS - Oasis

## Les grandes lignes du projet

Dans le cadre du PI Oasis, nous développons une architecture réseau qui connecte :
- des clients : devant chaque salle de la Mine est disposé un écran tactile qui regroupe différentes informations sur la salle :
    - données physiques (température, humidité, taux de CO2)
    - données de disponibilité (emploi du temps sur la journée)
- un serveur central qui relève les données de disponibilité sur Oasis et qui procède à certains calculs

Le dépôt git contient le code qui gère l'interface Oasis/serveur et serveur/client, côté serveur.

Le serveur est un serveur Webscoket, connecté du côté du client via NodeRed. On ne développe en 🐍`python` que la partie serveur.


## Le dépôt git

Ce dépôt git contient principalement les éléments :

  - [🗒️ `README.md`](README.md) : description du projet (ce document)
  - [📁 `serveur`](serveur) : différents fichiers qui gèrent le côté serveur du projet. Ces fichiers sont présents une RaspberryPi qui fait le lien entre Oasis et les écrans tactiles (clients) disposés devant les salles. Le serveur procède aussi au calcul du choix de la salle après une requête du client.
    - [🐍 `app.py`](serveur/app.py) : fichier principal du serveur\
    Et trois fichiers python qui définissent différentes méthodes
    - [🐍 `school.py`](serveur/backend/school.py) : gère la classe `School` qui regroupe les classes `Room` et déclenche le scrapping d'Oasis
    - [🐍 `room.py`](serveur/backend/room.py) : gère la classe `Room` qui contient l'emploi du temps de chaque salle et contrôle l'envoi des informations aux clients
    - [🐍 `scrap_oasis.py`](serveur/backend/scrap_oasis.py) : code support du scrapping d'Oasis

Par ailleurs, les dossiers [📁 `scrapping`](scrapping) et [📁 `communication_client_serveur`](communication_client_serveur) contienent des brouillons, des fichiers de code qui ont servi à différents tests lors du développement. Ils n'ont pas vocation à rester dans le dépôt.

## Vocabulaire et règles de la disponibilité

Une salle peut posséder trois statuts (non mutuellement exclusifs) :
- 🔴 **réservée :** Oasis indique (modulo le temps de rafraîchissement des données) que la salle est reservée
- **🔴 occupée :** deux cas :
  - la salle n'est *pas réservée* mais quelqu'un est dedans
  - la salle est *reservée* (on considère que toute salle reservée est indisponible)
- 🟢 **libre :** la salle n'est pas reservée et personne n'est dedans

Si je veux me rendre dans une salle, je peux :
- aller dans une salle **🔴 réservée** si c'est moi qui ai effectué la reservation
- aller dans une salle **🟢 libre** (donc non réservée, non occupée) et indiquer sur l'écran ma présence dans la salle, qui sera désormais marquée **🔴 ocupée**