# 📁 Serveur

Ce code est présent sur la Raspberry centrale servant de serveur.

# Fonctionnement général

Le fichier [🐍 `app.py`](app.py) contient le code qui fait tourner le serveur.

Le serveur est lancé sur le réseau Movie, il s'agit d'un serveur WebSocket.

Les informations liées aux disponibilités des salles sont regroupées dans la classe `School`, définie dans le [📁 `backend`](backend). Elle est initialisée en même temps que le lancement du serveur.

A chaque nouvelle connection, le client (une salle) est stocké dans une classe `Room`, définie dans le [📁 `backend`](backend). 

Le premier client à se connecter est identifié comme tel et sera chargé, périodiquement, d'actualiser les données de disponibilité (en scrappant Oasis) et en les envoyant à tous les clients connectés au serveur.

Par ailleurs, le serveur gère deux types de requêtes envoyées par les clients :
- la demande d'une salle libre selon un certain nombre de critères (géré par la classe `School`), et l'envoi de la salle choisie au client
- le fait d'indiquer une salle effectivement occupée (lorsqu'une personne rentre dans une salle, elle indique sur l'écran qu'elle est effectivement présente et l'information remonte au serveur)


## Fonctionnement du [📁 `backend`](backend)

Le [📁 `backend`](backend) comporte 3 fichiers 🐍 `python` qui gèrent les méthodes appliquées dans [🐍 `app.py`](app.py) :
- [🐍 `room.py`](backend/room.py) qui définit une salle (classe `Room`), stocke la connection WebSocket, envoie les updates des réservations et tient le registre des disponibilités de la salle.
- [🐍 `school.py`](backend/school.py) qui regroupe toutes les salles (dans la classe `School`), gère le scrapping pour récupérer les données sur Oasis et gère le calcul des salles disponibles, proches
- [🐍 `scrap_oasis.py`](backend/scrap_oasis.py) qui définit la fonction `scrap` chargée de récupérer, via scrapping, les données de l'emploi du temps du jour. Cette fonction actualise la classe `School` qui actualise les données des `Room`. Il faut récupérer le webdriver de chromium avec la commande :

        sudo apt-get install chromium-webdriver


## Fonctionnement du [📁 `room_priorities`](backend/room_priorities)

Le [📁 `room_priorities`](backend/room_priorities) comporte 2 fichiers 🐍 `python` :
- [🐍 `roomDict.py`](backend/room_priorities/roomDict.py) qui stocke les informations inhérentes aux salles (capacité, équipement etc.). Le dictionnaire est utilisé dans [🐍 `roomPrioriry.py`](backend/room_priorities/roomPriority.py)
- [🐍 `roomPrioriry.py`](backend/room_priorities/roomPriority.py) qui regroupe, pour chaque salle, la liste des autres salles, triées par proximité (priorité)