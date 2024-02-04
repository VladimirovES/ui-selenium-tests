FROM python:3.11-slim-buster

RUN apt update && apt install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \
    && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
    && apt update \
    && apt -y install docker-ce

WORKDIR /simple_solution_ui_test/
COPY ./ /simple_solution_ui_test/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN apk add -u zlib-dev jpeg-dev gcc musl-dev
RUN python -m pip install pip==22.1.2 && pip install wheel && pip install --upgrade wheel \    
    && pip install --upgrade cython \
    && pip install coincurve  \
    && pip install --upgrade setuptools \
    && pip install -r requirements.txt \
