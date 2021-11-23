# Headbang


APIDoc: http://localhost:8000/redoc

Luigi: http://localhost:8082

Kibana: http://localhost:5601


## Install

Docker

```bash
docker-compose down && docker-compose up -d --build && docker-compose logs -t -f
```

Local

```bash
pyenv virtualenv 3.10.0 headbang
pyenv activate headbang
pip install --upgrade -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 80 --reload --log-level debug
```


## Luigi jobs

```bash
PYTHONPATH='.' python -m luigi --module app.tasks.spotify FollowedArtists --local-scheduler
```
