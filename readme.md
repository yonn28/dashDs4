<img src="assets/long_child.jpg" alt="Children" width="1000" height="140">

<!-- TEAM LOGO -->
<br />
<p align="center">
  <a href="https://github.com/yonn28/dashDs4">
    <img src="assets/Team79Logo_black.png" alt="Logo" width="100" height="130">
  </a>

  <h2 align="center">KidNutrilytics</h2>
  
  <p align="center">
   <img src="assets/correlation.png" alt="Correlation" width="150" height="40">
  </p>
  <h4 align="center">DS4A Colombia Project</h4>

  <p align="center">
    The ultimate platform to predict malnutrition and its relapse in children under five years of age. Our ML models were fitted with 800.000+ registers of children at ICBF.
    <br />
    <a href="https://github.com/yonn28/dashDs4"><strong>Explore the GitHub Repo» </strong></a>
  </p>
</p>


## Built With 🛠️

* [Dash-Plotly](https://dash.plotly.com/)
* [GCP](https://cloud.google.com/)

<!-- GETTING STARTED -->
## Deployment 🚀

1. Clone the repo
   ```sh
   git clone https://github.com/yonn28/dashDs4.git
   ```
2. Create virtual enviroment (please verify you have venv in your system)
   ```
   python3 -m venv dashDS4
   ```
3. Activate virtual enviroment 

   ```
   source dashDS4/bin/activate 
   ```

4. install dependencies

   ```
   python3 -m pip install -r requirements.txt

   ```
5. Run proyect
   ```
   python3 main.py
   ```
6. In case you install a new dependencies, update requirements.txt

   ```
   python3 -m  pip freeze > requirements.txt

   ```
### Docker testing local

```
docker build -t docker-ds4 .
docker run docker-ds4 -p 8080:8080
```
##### It's exposed at 8080 port in localhost

### Deploy GCP by hand

1. Setting default region

```
gcloud config set run/region northamerica-northeast1
 
 ```
2. Setting gcloud google container registry

```
gcloud builds submit --tag gcr.io/ds4all-deploy/dash-ds4-examaple  --project=ds4all-deploy
```

3. Setting deploy with cloud run

```
gcloud run deploy --image gcr.io/ds4all-deploy/dash-ds4-examaple --platform managed  --project=ds4all-deploy --allow-unauthenticated --memory=8Gi --cpu=2
```

4. Creating user for github actions please configure secrets with this info

https://medium.com/google-cloud/how-to-deploy-your-cloud-run-service-using-github-actions-e5b6a6f597a3


<!-- CONTACT -->
## Authors ✒️

* **Daniel Ramírez** 
* **David Quintero**
* **Julián Monsalve**
* **Natalia Monroy**
* **Nicolás Cabrera**
* **Yonny Nova**

