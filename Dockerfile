FROM python:3.10.0-slim-buster@dcb11f3b86fe8d4f6974f86da61b331e6ed465a0b3602eacd031dcf41070c4f4
COPY ./src /
ENV FLASK_APP="app"
ENV FLASK_ENV="production"
EXPOSE 5000
CMD litestream replicate -exec "python -m flask run"
