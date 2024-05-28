#FROM python:3.12-slim as builder
#
#RUN python3 -m venv /venv && /venv/bin/pip install -U pip wheel setuptools && mkdir /src && mkdir /src/src
#
#COPY src/backend/pyproject.toml /src/
#
#
#FROM python:3.12-slim
#
#WORKDIR /src
#COPY --from=builder /venv /venv
#COPY src /src/src
#
#CMD ["/venv/bin/fastapi", "dev","backend.__main__"]

FROM python:3.12-slim as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY ./src/backend/pyproject.toml ./src/backend/poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12-slim
WORKDIR /code
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src/backend /code/backend

CMD ["fastapi", "run", "backend/__main__.py", "--port", "80"]