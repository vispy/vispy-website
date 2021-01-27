# mypaas.service = vispy-redirect
# mypaas.url = https://api.vispy.org
# mypaas.maxmem = 100m


FROM python:3.8-slim-buster

RUN apt update \
    && pip --no-cache-dir install pip --upgrade \
    && pip --no-cache-dir install uvicorn asgineer

WORKDIR /root
COPY . .
CMD ["python", "server.py"]
