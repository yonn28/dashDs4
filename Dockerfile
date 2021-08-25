FROM python:3.8

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./


ENV MODEL_DIR=/assets/models
ENV MODEL_FILE_MALN=Modelo_malnutrition.sav
ENV MODEL_FILE_RELP=Modelo_relapse.sav

RUN python -m pip install -r requirements.txt

EXPOSE 8080

CMD python main.py  
