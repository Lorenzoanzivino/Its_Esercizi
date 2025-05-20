FROM python:3.11.11

COPY python_requirements.txt /
RUN pip install -r python_requirements.txt

RUN mkdir /app

#COPY . nomecartella
'''prende tutto ciò che sta dentro la cartella
esempio cartella : 
ESERCIZIO/
    - Dockerfile
    - Cartella_File/
        - file.py
        - file2.py
        - file3.py
    - file_main.py

COPY . /app'''

COPY app.py /app
WORKDIR /app