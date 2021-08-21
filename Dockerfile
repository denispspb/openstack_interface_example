FROM python:latest

RUN python -m pip install openstacksdk

COPY . /local/integration_test_suite
WORKDIR /local/integration_test_suite

CMD python run_integration_test.py

