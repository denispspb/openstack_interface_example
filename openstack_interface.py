from openstack.connection import Connection
from openstack.exceptions import ConflictException, BadRequestException

class OpenStackConnectorException(Exception):
    pass

class OpenStackConnector:
    """
    An interface for operating with virtual machines located in the OpenStack
    """

    def __init__(self, url, username, password, project_name, project_domain_name, user_domain_name, region_name):
        self.connection = Connection(region_name=region_name,
                                     auth=dict(auth_url=url, username=username, password=password,
                                                 project_name=project_name, project_domain_name=project_domain_name, user_domain_name=user_domain_name),
                                     identity_api_version="3")
    
    def close_connection(self):
        """
        Release any resources held open by the API connection
        """
        self.connection.close()
    
    def vm_power(self, vm_name, state):
        """
        Powering on/off the vm given
        :param vm_name: str
        :param state: str, either on or off
        :return: bool, True if vm exists, False otherwise
        """
        states = ["on", "off"]
        if state not in states:
            raise OpenStackConnectorException(f"Incorrect action was provided for the vm {vm_name} power state change")
        
        vm_id = self._get_vm_id_by_name(vm_name)

        if not vm_id:
            return False
        
        try:
            if state == "on":
                self.connection.compute.start_server(vm_id)
            else:
                self.connection.compute.stop_server(vm_id)
        except ConflictException: # This exception block handles the situation when the VM is already in the required power state
            pass
        
        return True
    
    def change_ram_qty(self, vm_name, size_mb):
        """
        Changing the amount of RAM for the vm given
        :param vm_name: str
        :param size_mb: int, the required amount of memory in megabytes
        """
        vm_id = self._get_vm_id_by_name(vm_name)
        flavor_id = self.connection.get_flavor_by_ram(size_mb).id

        try:
            self.connection.compute.resize_server(vm_id, flavor_id)
        except BadRequestException: # This exception block handles the situation when such flavor already assigned on the host
            pass
    
    def _get_vm_id_by_name(self, vm_name):
        """
        Obtain the VM id using the name given
        :param vm_name: str
        :return: str, VM's id
        """
        vm_info = self.connection.compute.find_server(vm_name)
        return (vm_info.id if vm_info else None)
    
    def get_all_vms(self):
        """
        Obtain the list of all VMs available in the OpenStack project
        :return: list, all available vms' names
        """
        available_servers = self.connection.compute.servers()
        if available_servers:
            vm_names = [server.name for server in available_servers]
            return vm_names
        else:
            return []

