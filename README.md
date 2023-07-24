# Accessible Cities API
This is a Flask API that requests OSM's Overpass data on cities' accessibility features like wheelchair adaptations. It processes the data and compares two cities according to 6 criteria.

Each value is expressed in a percentage obtained with the total amount of nodes recovered from OSM and the quantity of them which have been tagged with a specific accessibility feature (erg. "wheelchair").

## Purpose

This API was created with the goal to obtain and processing data that will be passed to a widget.
The widget belongs to a website that compares life in two cities according to several points of view (prices, transportation, etc.)

But the project could be used or adapted for other projects that contribute to improving people's lives given a condition of disability.

### Json response samples

The image represents a successful response that returns the accessibility data on two cities:

![Screenshot 2023-06-27 at 13-48-19 Screenshot](https://github.com/gabyfdez90/accessibleCitiesAPI/assets/117080861/0203da5d-708c-4d34-85d2-3153d747e599)

The image represents a failed response when one of the cities is spelled incorrectly or doesn’t appear in the OSM database.

![Screenshot 2023-06-27 at 13-49-08 Screenshot](https://github.com/gabyfdez90/accessibleCitiesAPI/assets/117080861/7d292dc3-6531-4a79-8a6e-da7614c3c93f)

## Technologies
* Python
* Flask
* API Rest
* Thunder
* GIT
* Redis

### Redis, a caching database
In order to improve response times by decreasing the number of requests made to Overpass API, this code first checks if the given city has been already requested in the same session. 

In that case, the data of that city should be on a local Redis caching system, so the response time for that endpoint could be dramatically reduced.

Important note: For this code works just as written in the repo, the local machine that runs it needs to run also a Redis service. If any user wants to clone this project and use it they will need to install/run Redis locally, or make some changes in the “app/__init__.py” file, for example.

## Installation and local deploy
This is a suggested set of instructions to run locally the Accessible Cities API:

* Install and run the Redis caching database
* Clone the project from this repo
* Create a virtual environment
*Install the requirements on the “requeriments.txt” file
* Execute `flask run`
* Try running an endpoint like “http://locahost:5000/api/Madrid/Barcelona” in Thunder, Postman, or a web browser

## Contributors
* [Jéssica Ríos](https://github.com/JessRm04)
* [Gabriela M. Fernández](https://github.com/gabyfdez90)
