FROM mcr.microsoft.com/playwright/python:v1.58.0-jammy
WORKDIR /app
COPY . .
RUN pip install playwright
CMD ["python", "main.py"]
