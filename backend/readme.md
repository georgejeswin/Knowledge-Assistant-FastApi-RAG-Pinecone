python -m uvicorn app.main:app --reload

celery -A app.workers.celery_app worker --loglevel=info

To Activate venv
venv\Scripts\activate

Swagger - http://127.0.0.1:8000/docs
Redoc - http://127.0.0.1:8000/redoc