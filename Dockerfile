FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY ./main.py /app/main.py

RUN pip install requests

CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "4200"]
