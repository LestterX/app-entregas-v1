FROM debian

LABEL app="App Entregas V1"
USER root

WORKDIR /app-entregas
COPY . /app-entregas/

EXPOSE 5050

RUN apt-get update &&\ 
    apt-get upgrade -y &&\
    apt-get install python3 python3-pip -y &&\
    python3 -m pip install -r ./requirements.txt --break-system-packages

ENTRYPOINT [ "python3", "main.py" ]