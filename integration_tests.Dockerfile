FROM python:3-alpine

WORKDIR /build
RUN pip install pipenv
COPY Pipfile* /build/
RUN pipenv install --system --dev \
 && rm -rf /build

WORKDIR /app
COPY ./pytest.ini pytest.ini
COPY ./integration_tests/ ./

CMD python -m pytest
