FROM python:3.11-slim-buster

WORKDIR /ui-selenium-tests/
COPY ./ /ui-selenium-tests/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install pip==22.1.2 && pip install wheel && pip install --upgrade wheel \
    && pip install --upgrade cython \
    && pip install coincurve  \
    && pip install --upgrade setuptools \
    && pip install -r requirements.txt
