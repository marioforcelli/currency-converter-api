FROM python:3.13-alpine


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt
# COPY ./.env /code/.env


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]