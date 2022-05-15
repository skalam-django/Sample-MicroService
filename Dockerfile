FROM python:3.9
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /sample_microservice/
COPY src /sample_microservice/src
RUN pip3 install --upgrade pip
RUN pip3 install wheel
RUN pip3 install -r /sample_microservice/requirements.txt --no-cache-dir
WORKDIR /sample_microservice/src