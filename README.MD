# MOCK AIRFLOW DAG

## STEPS TO RUN PROJECT

Clone project from GitHub to local directory
```bash
git clone git@github.com:i-wizard/mock-airflow-dag.git
```
Change directory to project root
```bash
cd mock-airflow-dag
```
## With Docker (recommended)
Ensure you have docker installed on your machine
```bash
docker-compose up --build
```
## Without Docker
Create and activate virtual environment using `Python >=v3.10.0`
```bash
python -m venv venv && source venv/bin/activate
```
Install project dependencies
```bash
pip install -r requirements.txt
```
Run DB migrations (this creates an SQLite DB)
```bash
python manage.py migrate
```
Run server on default port 8000
```bash
python manage.py runserver
```

### View Project
Visit http://localhost:8000/swagger/ as the API playground (interface) to view and test API endpoints

#### Run Integration tests
With Docker
```bash
docker-compose run --rm web pytest -vv
```
Without Docker
```bash
pytest -vv
```


