FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy
WORKDIR /app
COPY . .
RUN pip install playwright
CMD ["python", "main.py"]
```

`requirements.txt`:
```
playwright
