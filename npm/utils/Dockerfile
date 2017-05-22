FROM python:3.4
ADD . /code
WORKDIR /code
RUN apt-get update
RUN apt-get install -qq libmysqlclient-dev
RUN apt-get install -qq python-dev
RUN pip3 install -r requirements.txt
CMD ["python", "npm_crawler.py"]