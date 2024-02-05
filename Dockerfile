FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

# Install python and sqlite dependencies under a virtual package
RUN apk --no-cache add sqlite
WORKDIR /db

# Install requirements
COPY ../requirements.txt /requirements.txt
RUN pip install --upgrade pip -r /requirements.txt

# Delete virtual packages as we installed our dependencies
# RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./ /app

#COPY ./wait-for /bin/wait-for
#RUN chmod 777 -R /bin/wait-for

RUN adduser -D user
USER user


COPY ../db.sqlite3 /db/
CMD ["sqlite3", "/data/initial-db.sqlite"]
