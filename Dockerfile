FROM mcr.microsoft.com/playwright/python:v1.48.0-focal

WORKDIR /tests

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY pytest.ini .
COPY ./tests .

CMD ["pytest", "-m", "e2e", "-vv"]