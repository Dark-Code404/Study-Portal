
FROM python:3.13-alpine
 

RUN mkdir /app
 

WORKDIR /app
 

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1 
 

RUN python -m pip install --upgrade pip 
 

COPY requirements.txt  /app/
 

RUN python -m pip install --no-cache-dir -r requirements.txt
 

COPY . /app/
 

EXPOSE 8000
 

ENTRYPOINT ["sh", "build.sh"]