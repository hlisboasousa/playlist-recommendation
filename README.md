## Henrique Lisboa de Sousa

## General Goal

In this project, we will design, implement and deploy a playlist recommendation service built on microservices, combining a Web front end and a machine learning module. The service will be built and tested using continuous integration, and automatically deployed using continuous delivery. The practice of integrating a machine learning workflow with DevOps has been referred to as MLOps.

We will obtain experience using some of the most popular tools in this context: Docker to containerize application components, Kubernetes to orchestrate the deployment in a cloud environment, GitHub as a central code repository, and ArgoCD as the continuous delivery framework on top of Kubernetes.

We will create a recommendation system to recommend playlists to a user based on a set of songs that the user listened in the past.

## Tecnologies

Frontend:
    HTML, CSS, JS,
    Jest

Backend:
    Flask,
    Poetry,
    Unittest,
    Pandas
    Mlxtend - Apriori

## Dataset

We will use a (small) sample of a Spotify dataset. The dataset sample is available on the cluster at /home/datasets/spotify-sample (in the VM's root file system, not HDFS). It includes two parts:

    The playlists-sample-ds1.csv and playlists-sample-ds2.csv datasets contain 500 playlists each. The two datasets represent the set of playlists in the platform and can be used to emulate an update to the model.

    The songs.csv file contains songs in the playlists that can be used in the recommendation step.

    You can first train your model using playlists-sample-ds1.csv and later update the model using playlists-sample-ds2.csv.

## How to run: Backend
    python3 models/itemsets_generator.py
    poetry install
    poetry run flask --app api/app.py run

## How to run: Frontend
    cd frontend
    python3 -m http.server 8000 
