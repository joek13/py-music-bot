FROM python:3.8.12-slim-buster

# copy python files over
COPY . /app
WORKDIR /app

# install ffmpeg
RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y

# instal python dependencies
RUN pip install pipenv
RUN pipenv install

# run musicbot
CMD [ "pipenv", "run", "python", "-m", "musicbot" ]