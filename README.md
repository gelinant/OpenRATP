# OpenRATP
Projet Python EIG-2101 ESIEE Paris


Ce projet Python permet d'analyser les données en OpenData D'Ile de France Mobilités (anciennement STIF, agences des transports parisiens)

Le programme a besoin de CSV fournis par le STIF pour fonctionner. Vous pouvez les télécharger à l'adresse suivante :
* [Validation du 1er semestre de l'année en cours](https://opendata.stif.info/explore/dataset/validations-sur-le-reseau-ferre-nombre-de-validations-par-jour-1er-sem/)
* [Validation du 2eme semestre de l'année en cours](https://opendata.stif.info/explore/dataset/validations-sur-le-reseau-ferre-nombre-de-validations-par-jour-2e-sem/)

*Vous devez renseigner une [clef d'API Google Maps Geocode](https://developers.google.com/maps/documentation/geocoding/get-api-key) dans le fichier [config.py](config.py) pour utiliser la fonction de localisation des stations*


Les données sont fournies sous la version francaise de la licence ODbL