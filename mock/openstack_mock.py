from urllib.parse import urlparse
import json

class OpenStackMock:

    def return_api_info(self, request):
        """
        :param request: Flask Request class object
        """
        host_root = self._get_host_root_url(request.base_url)
        response_json = {
            "versions": {
                "values": [{
                    "id": "v3.14", 
                    "status": "stable", 
                    "updated": "2020-04-07T00:00:00Z", 
                    "links": [{
                        "rel": "self",
                        "href": f"{host_root}v3/"
                    }], 
                    "media-types": [{
                        "base": "application/json", 
                        "type": "application/vnd.openstack.identity-v3+json"
                    }]
                }]
            }
        }
        return 300, json.dumps(response_json)
    
    def login(self, request):
        """
        :param request: Flask Request class object
        """
        host_root = self._get_host_root_url(request.base_url)
        username_provided = request.json["auth"]["identity"]["password"]["user"]["name"]
        password_provided = request.json["auth"]["identity"]["password"]["user"]["password"]
        if username_provided == "test-user" and password_provided == "12345":
            response_json = {
                "token": {
                    "methods": ["password"], 
                    "user": {
                        "domain": {
                            "id": "9b5b3a5decdb4741892cfcf32c3a79f1", 
                            "name": "somedomain.com"}, 
                            "id": "f34ce3bc9b96aa7fe12c40f0db2ffda632dac55b16066e7aad636b7c19524a09", 
                            "name": "test-stands-openstack", "password_expires_at": None
                        }, 
                    "audit_ids": ["tyQp35AzT56yCwYPMmNC2g"], 
                    "expires_at": "2121-08-12T16:56:52.000000Z", 
                    "issued_at": "2121-08-11T14:56:52.000000Z", 
                    "project": {
                        "domain": {
                            "id": "9b5b3a5decdb4741892cfcf32c3a79f1", 
                            "name": "somedomaingroup.com"
                        }, 
                        "id": "aeea0ca2b1ab449e86fd7b4295455ecf", 
                        "name": "stands"
                    }, 
                    "is_domain": False, 
                    "roles": [
                        {
                            "id": "330b6d834dc24dedb44ae187c6b1bb3e", 
                            "name": "reader"
                        }, 
                        {
                            "id": "a95509e1b0dd494f9d6027b8362f6934", 
                            "name": "member"
                        }
                    ], 
                    "catalog": [
                        {
                            "endpoints": [
                                {
                                    "id": "1b38b2bb2b024bc19609073648d26e59", 
                                    "interface": "public", 
                                    "region_id": "eu1", 
                                    "url": f"{host_root}v2.1", 
                                    "region": "eu1"
                                }, 
                                {
                                    "id": "677ce4bcd38c4610b758200f181dccf3", 
                                    "interface": "internal", 
                                    "region_id": "eu1", 
                                    "url": "http://localhost-internal:8774/v2.1", 
                                    "region": "eu1"
                                }, 
                                {
                                    "id": "c8e1d120edbc4237a34a555befeaeb4b", 
                                    "interface": "admin", 
                                    "region_id": "eu1", 
                                    "url": "http://localhost-admin:8774/v2.1", 
                                    "region": "eu1"
                                }
                            ], 
                            "id": "37a32ec4c43e43eb9a3e7e7920687f33", 
                            "type": "compute", 
                            "name": "nova"
                        }
                    ]
                }
            }
            code = 201
            custom_headers = {"X-Subject-Token": "gAAAAABhE-6wVsZdpGzbcZUej"}
        else:
            response_json = {"text": "Invalid credentials were provided"}
            code = 401
            custom_headers = None
    
        return code, json.dumps(response_json), custom_headers
    
    def return_compute_api_info(self, request):
        """
        :param request: Flask Request class object
        """
        host_root = self._get_host_root_url(request.base_url)
        response_json = {
            "version": {
                "id": "v2.1", 
                "status": "CURRENT", 
                "version": "2.87", 
                "min_version": "2.1", 
                "updated": "2013-07-23T11:33:21Z", 
                "links": [
                    {
                        "rel": "self", 
                        "href": f"{host_root}v2.1/"
                    }, 
                    {
                        "rel": "describedby", "type": "text/html", 
                        "href": "http://docs.openstack.org/"
                    }
                ], 
                "media-types": [
                    {
                        "base": "application/json", 
                        "type": "application/vnd.openstack.compute+json;version=2.1"
                    }
                ]
            }
        }

        return 200, json.dumps(response_json)
    
    def return_flavors(self, request):
        """
        :param request: Flask Request class object
        """
        host_root = self._get_host_root_url(request.base_url)
        response_json = {
            "flavors": [
                {
                    "id": "13c5cccf-f907-4861-b367-bee86bec47cd", 
                    "name": "test.1.4", 
                    "ram": 4096, 
                    "disk": 60, 
                    "swap": "", 
                    "OS-FLV-EXT-DATA:ephemeral": 0, 
                    "OS-FLV-DISABLED:disabled": False, 
                    "vcpus": 1, 
                    "os-flavor-access:is_public": False, 
                    "rxtx_factor": 1.0, "links": [
                        {
                            "rel": "self", 
                            "href": f"{host_root}v2.1/flavors/13c5cccf-f907-4861-b367-bee86bec47cd"
                        }, 
                        {
                            "rel": "bookmark", 
                            "href": f"{host_root}flavors/13c5cccf-f907-4861-b367-bee86bec47cd"
                        }
                    ], 
                    "description": None, 
                    "extra_specs": {}
                }, 
                {
                    "id": "45176848-8402-44de-8b19-90952025db9e", 
                    "name": "test.1.8", 
                    "ram": 8192, 
                    "disk": 60, 
                    "swap": "", 
                    "OS-FLV-EXT-DATA:ephemeral": 0, 
                    "OS-FLV-DISABLED:disabled": False, 
                    "vcpus": 1, 
                    "os-flavor-access:is_public": False, 
                    "rxtx_factor": 1.0, 
                    "links": [
                        {
                            "rel": "self", 
                            "href": f"{host_root}v2.1/flavors/45176848-8402-44de-8b19-90952025db9e"
                        }, 
                        {
                            "rel": "bookmark", 
                            "href": f"{host_root}flavors/45176848-8402-44de-8b19-90952025db9e"
                        }
                    ], 
                    "description": None, 
                    "extra_specs": {}
                }
            ]
        }

        return 200, json.dumps(response_json)
    
    def return_extra_specs_for_flavor(self, id):
        """
        :param id: str, flavor's id
        """
        known_flavors = ["13c5cccf-f907-4861-b367-bee86bec47cd", "45176848-8402-44de-8b19-90952025db9e"]
        if id in known_flavors:
            response_json = {"extra_specs": {}}
            code = 200
        else:
            response_json = {"text": "Unknown flavor's info was requested"}
            code = 404
    
        return code, json.dumps(response_json)
    
    def return_server_info(self, request):
        """
        :param request: Flask Request class object
        """
        host_root = self._get_host_root_url(request.base_url)
        if 'name' in request.args:
            server_name = request.args.get('name')
        else:
            return 400, json.dumps({"text": "No suitable filters were provided in the request"})
    
        if server_name == 'test-host':
            response_json = {
                "servers": [
                    {
                        "id": "a4338c32-7aeb-4a11-880a-3fe4d559a341", 
                        "name": "test-host", 
                        "links": [
                            {
                                "rel": "self", 
                                "href": f"{host_root}v2.1/servers/a4338c32-7aeb-4a11-880a-3fe4d559a341"
                            }, 
                            {
                                "rel": "bookmark", 
                                "href": f"{host_root}servers/a4338c32-7aeb-4a11-880a-3fe4d559a341"
                            }
                        ]
                    }
                ]
            }
            code = 200
        else:
            response_json = {"text": "Unknown server name was provided"}
            code = 404
    
        return code, json.dumps(response_json)
        
    def apply_action_on_server(self, id, request):
        """
        :param id: str, server's id
        :param request: Flask Request class object
        """
        known_servers_ids = ["a4338c32-7aeb-4a11-880a-3fe4d559a341"]
        supported_actions = ["os-start", "os-stop", "resize"]
        if id in known_servers_ids:
            if [key for key in request.json.keys() if key in supported_actions]:
                response_json = {"text": "Action was applied on the server"}
                code = 202
            else:
                response_json = {"text": "Unknown action code was provided"}
                code = 400
        else:
            response_json = {"text": "Unknown server id was provided"}
            code = 404
    
        return code, json.dumps(response_json)
    
    def _get_host_root_url(self, url):
        """
        Obtain the host root URL from request.base_url value
        """
        parse_result = urlparse(url)
        return f"{parse_result.scheme}://{parse_result.netloc}/"

