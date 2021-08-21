# OpenStack Interface Example
A simple OpenStack interface based on python openstacksdk lib with integration test example (mocked OpenStack API included).
____
## Prerequisites 
If you wish to run this code outside Docker containers, you will need python 3 interpreter and flask/openstacksdk libraries. The easiest way to install them is to run pip against the requirements.txt file, see the example below:
```
$ python3 -m pip install -r requirements.txt
```
You can also run the code inside Docker containers, for this you will need docker-ce package installed on your Linux OS or Docker Desktop application for Windows.
___
## Usage
### Running the code manually
First of all, change directory to mock and run OpenStack mocked REST API using the next command:
```
$ python3 run_openstack_rest.py
```
:speech_balloon: *This command will run the Flask server in foreground. Please run the integration tests file in the separate window or use any terminal multiplexer for convenience (screen, tmux, etc.)*

Now the mocked OpenStack REST API is up and running, and you can run the integration tests against it. Change directory to the code's root and start integration test with the next command:
```
$ python3 run_integration_test.py -osurl http://localhost:8774 -osusr test-user -ospwd 12345
```
The integration test results will appear on the screen:
```
2021-08-21 21:14:23,149 [INFO] [__init__] OpenStackConnector Integration Test Suite was initialized
2021-08-21 21:14:23,149 [INFO] [vm_power] Received the power change request (start) for the virtual machine test-host
2021-08-21 21:14:23,204 [INFO] [vm_power] Power state of the virtual machine test-host was successfully changed
2021-08-21 21:14:23,204 [INFO] [vm_power] Received the power change request (stop) for the virtual machine test-host
2021-08-21 21:14:23,226 [INFO] [vm_power] Power state of the virtual machine test-host was successfully changed
2021-08-21 21:14:23,226 [INFO] [change_vm_ram] Received the RAM change request (7168) for the virtual machine test-host
2021-08-21 21:14:23,258 [INFO] [change_vm_ram] The amount of RAM on the virtual machine test-host was successfully changed
2021-08-21 21:14:23,258 [INFO] [__del__] OpenStackConnector Integration Test was finished
```
You can also check the Flask's logs in the other terminal window, there you will see the information about all the endpoints used by the openstacksdk to perform the actions above:
```
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET / HTTP/1.1" 300 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "POST /v3/auth/tokens HTTP/1.1" 201 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET /v2.1 HTTP/1.1" 200 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET /v2.1/servers/test-host HTTP/1.1" 404 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET /v2.1/servers?name=test-host HTTP/1.1" 200 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "POST /v2.1/servers/a4338c32-7aeb-4a11-880a-3fe4d559a341/action HTTP/1.1" 202 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET / HTTP/1.1" 300 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "POST /v3/auth/tokens HTTP/1.1" 201 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET /v2.1 HTTP/1.1" 200 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET /v2.1/servers/test-host HTTP/1.1" 404 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET /v2.1/servers?name=test-host HTTP/1.1" 200 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "POST /v2.1/servers/a4338c32-7aeb-4a11-880a-3fe4d559a341/action HTTP/1.1" 202 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET / HTTP/1.1" 300 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "POST /v3/auth/tokens HTTP/1.1" 201 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET /v2.1 HTTP/1.1" 200 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET /v2.1/servers/test-host HTTP/1.1" 404 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET /v2.1/servers?name=test-host HTTP/1.1" 200 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET /v2.1/flavors/detail?is_public=None HTTP/1.1" 200 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET /v2.1/flavors/13c5cccf-f907-4861-b367-bee86bec47cd/os-extra_specs HTTP/1.1" 200 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "GET /v2.1/flavors/45176848-8402-44de-8b19-90952025db9e/os-extra_specs HTTP/1.1" 200 -
127.0.0.1 - - [21/Aug/2021 21:14:23] "POST /v2.1/servers/a4338c32-7aeb-4a11-880a-3fe4d559a341/action HTTP/1.1" 202 -
```
### Running the code inside the Docker containers
First of all, build Docker images using the next command:
```
$ docker-compose build
```
It will build two images, one for OpenStack REST API mock and one for the Integration test respectively. When the build is done you will see the next two images inside the Docker:
```
$ docker images
REPOSITORY                          TAG       IMAGE ID       CREATED          SIZE
openstackconnectorintegrationtest   latest    01d320ff792d   41 minutes ago   955MB
openstackmock                       latest    ae6eb7051134   44 minutes ago   922MB
```
Now you can run both the mock and integration test simultaneously by using the next command:
```
$ docker-compose up
```
You will see logs of the integration test and Flask server in your terminal. They will contain all the actions made by the openstacksdk and all the endpoint it used to to perform these actions:
```
integration_test_suite_1  | 2021-08-21 18:23:29,304 [INFO] [__init__] OpenStackConnector Integration Test Suite was initialized
integration_test_suite_1  | 2021-08-21 18:23:29,304 [INFO] [vm_power] Received the power change request (start) for the virtual machine test-host
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET / HTTP/1.1" 300 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "POST /v3/auth/tokens HTTP/1.1" 201 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET /v2.1 HTTP/1.1" 200 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET /v2.1/servers/test-host HTTP/1.1" 404 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET /v2.1/servers?name=test-host HTTP/1.1" 200 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "POST /v2.1/servers/a4338c32-7aeb-4a11-880a-3fe4d559a341/action HTTP/1.1" 202 -
integration_test_suite_1  | 2021-08-21 18:23:29,358 [INFO] [vm_power] Power state of the virtual machine test-host was successfully changed
integration_test_suite_1  | 2021-08-21 18:23:29,358 [INFO] [vm_power] Received the power change request (stop) for the virtual machine test-host
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET / HTTP/1.1" 300 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "POST /v3/auth/tokens HTTP/1.1" 201 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET /v2.1 HTTP/1.1" 200 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET /v2.1/servers/test-host HTTP/1.1" 404 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET /v2.1/servers?name=test-host HTTP/1.1" 200 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "POST /v2.1/servers/a4338c32-7aeb-4a11-880a-3fe4d559a341/action HTTP/1.1" 202 -
integration_test_suite_1  | 2021-08-21 18:23:29,403 [INFO] [vm_power] Power state of the virtual machine test-host was successfully changed
integration_test_suite_1  | 2021-08-21 18:23:29,403 [INFO] [change_vm_ram] Received the RAM change request (7168) for the virtual machine test-host
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET / HTTP/1.1" 300 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "POST /v3/auth/tokens HTTP/1.1" 201 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET /v2.1 HTTP/1.1" 200 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET /v2.1/servers/test-host HTTP/1.1" 404 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET /v2.1/servers?name=test-host HTTP/1.1" 200 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET /v2.1/flavors/detail?is_public=None HTTP/1.1" 200 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET /v2.1/flavors/13c5cccf-f907-4861-b367-bee86bec47cd/os-extra_specs HTTP/1.1" 200 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "GET /v2.1/flavors/45176848-8402-44de-8b19-90952025db9e/os-extra_specs HTTP/1.1" 200 -
openstack_mock_1          | 172.22.0.3 - - [21/Aug/2021 18:23:29] "POST /v2.1/servers/a4338c32-7aeb-4a11-880a-3fe4d559a341/action HTTP/1.1" 202 -
integration_test_suite_1  | 2021-08-21 18:23:29,458 [INFO] [change_vm_ram] The amount of RAM on the virtual machine test-host was successfully changed
integration_test_suite_1  | 2021-08-21 18:23:29,458 [INFO] [__del__] OpenStackConnector Integration Test was finished
openstack_interface_example_integration_test_suite_1 exited with code 0
```
___
## Conclusion
It is an example of the openstacksdk lib usage and covering it with integration test. I stumbled with the problem of the test coding when I was adding my new automation of virtual machines maintenance to our Continuous Integration process. 
Feel free to use and expand it for your needs. I hope that it will be useful and you will spend less time than me when stumble with the same task. :v: