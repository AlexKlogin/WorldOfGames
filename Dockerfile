FROM python:3.7-alpine
        COPY . .
        RUN pip install Flask==0.10.1
        CMD python MainGame.py