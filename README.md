# FlaskAppTuto
Tutorial Flask App using Docker

# Goal
In this tutorial you will learn how to create a simple Flask App with MongoDB integration, deploy and run it inside a docker container using docker Compose

This App is based on http://containertutorials.com/docker-compose/flask-mongo-compose.html

# Files to be created in the app
├── app.py
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
└── templates
    └── todo.html

# Build and Run the Service using Docker Compose
$ docker-compose build
$ docker-compose up

# You can go to the browser and open the url http://localhost:5000 to see the HTML rendered
