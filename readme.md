# proyect for DS4

## instructions

## create virtual enviroment (please verify you have venv in your system)

***python3 -m venv dashDS4***

## activate virtual enviroment 

***source dashDS4/bin/activate***  

## install dependencies

***python3 -m pip install -r requirements.txt***

## copy base_final.csv

## run proyect

**python3 main.py**
## in case you install a new dependencies, update requirements.txt

***python3 -m  pip freeze > requirements.txt***

## Docker testing local

**docker build -t docker-ds4 .**

**docker run docker-ds4 -p 8080:8080**

it's expose at 8080 port in localhost

## deploy gcp by hand

### setting default region
***gcloud config set run/region northamerica-northeast1***
 
### setting gcloud google container registry
***gcloud builds submit --tag gcr.io/ds4all-deploy/dash-ds4-examaple  --project=ds4all-deploy***

### setting deploy with cloud run
***gcloud run deploy --image gcr.io/ds4all-deploy/dash-ds4-examaple --platform managed  --project=ds4all-deploy --allow-unauthenticated --memory=8Gi --cpu=2***

### creating user for github actions please configure secrets with this info

https://medium.com/google-cloud/how-to-deploy-your-cloud-run-service-using-github-actions-e5b6a6f597a3

