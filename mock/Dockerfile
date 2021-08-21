FROM python:latest

RUN python -m pip install flask

COPY . /local/mocked_openstack_api
WORKDIR /local/mocked_openstack_api

CMD python run_openstack_rest.py

