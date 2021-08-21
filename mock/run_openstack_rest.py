from flask import Flask, Response, request
from openstack_mock import OpenStackMock

app = Flask(__name__)

def response(code, data, custom_headers=None):
    return Response(
        status=code,
        mimetype="application/json",
        response=data,
        headers=custom_headers
    )

@app.route('/', methods=['GET'])
def return_api_info():
    code, text = openstack.return_api_info(request)
    return response(code, text)

@app.route('/v3/auth/tokens', methods=['POST'])
def login():
    code, text, headers = openstack.login(request)
    return response(code, text, headers)    

@app.route('/v2.1', methods=['GET'])
def return_compute_api_info():
    code, text = openstack.return_compute_api_info(request)
    return response(code, text)

@app.route('/v2.1/flavors/detail', methods=['GET'])
def return_flavors():
    code, text = openstack.return_flavors(request)
    return response(code, text)

@app.route('/v2.1/flavors/<string:id>/os-extra_specs', methods=['GET'])
def return_extra_specs_for_flavor(id):
    code, text = openstack.return_extra_specs_for_flavor(id)
    return response(code, text)
    
@app.route('/v2.1/servers', methods=['GET'])
def return_server_info():
    code, text = openstack.return_server_info(request)
    return response(code, text)

@app.route('/v2.1/servers/<string:id>/action', methods=['POST'])
def apply_action_on_server(id):
    code, text = openstack.apply_action_on_server(id, request)
    return response(code, text)

if __name__ == '__main__':
    openstack = OpenStackMock()
    app.run(host='0.0.0.0', port=8774, debug=True)

