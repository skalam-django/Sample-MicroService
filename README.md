# Sample Microservice

Sample Microservice: This is a sample microservice build in Python-Flask.


### Repo owner or admin

Sk Khurshid Alam

### Dependencies
* [**Python**](https://www.python.org/downloads/)
* [**Flask**](https://flask.palletsprojects.com/en/2.1.x/)
* [**Docker**](https://docs.docker.com/)

## Setup everything needed to run the server

**Build the Docker Image**
```
sudo docker build --no-cache -t sample_microservice .
```

**To Perform Unit Test**
```
sudo docker-compose run --rm --entrypoint "python -m unittest discover -p test.py" web
```

**Run Application using Docker Compose**
```
sudo docker-compose up
```

## Swagger Document
http://localhost:5000<br/>
**Note:** Change base url if application is running on different address<br/>

## Health Check:
http://localhost:5000/health_check<br/>
**Note:** Change base url if application is running on different address<br/>

## Sample Test
http://localhost:5000/api/v1/sample-api<br/>
**Note:** Change base url if application is running on different address<br/>
