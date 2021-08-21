import logging
import argparse
import os
from openstack_interface import OpenStackConnector

class OpenStackConnectorIntegrationTestSuiteException(Exception):
    pass

class OpenStackConnectorIntegrationTestSuite:
    """
    An integration test example for the OpenStackConnector
    """
    def __init__(self, os_url, os_user, os_password, os_project_name, os_project_domain_name, 
                os_user_domain_name, os_region_name):
        """
        os in vars stands for OpenStack
        :param os_url: str, OpenStack cluster connection URL
        :param os_user: str, username
        :param os_password: str, password
        :param os_project_name: str, project name where virtual machine instances being running
        :param os_project_domain_name: str, projects' domain name
        :param os_user_domain_name: str, user's domain name
        :param os_region_name: str, region name where OpenStack cluster is located
        """
        log_level = logging.INFO
        log_format = "%(asctime)s [%(levelname)s] [%(funcName)s] %(message)s"
        logging.basicConfig(format=log_format, level=log_level)

        self.os_url = os_url
        self.os_user = os_user
        self.os_password = os_password
        self.os_project_name = os_project_name
        self.os_project_domain_name = os_project_domain_name
        self.os_user_domain_name = os_user_domain_name
        self.os_region_name = os_region_name
        logging.info("OpenStackConnector Integration Test Suite was initialized")
    
    def __del__(self):
        """
        Finalizing integration testing by class' object deletion
        """
        logging.info("OpenStackConnector Integration Test was finished")

    def _openstack_connect(self):
        """
        Establishes connection to OpenStack
        :return: OpenStackConnector class' object
        """
        openstack_connector = OpenStackConnector(self.os_url, self.os_user, self.os_password, self.os_project_name,
                                                self.os_project_domain_name, self.os_user_domain_name, self.os_region_name)
        return openstack_connector
    
    def vm_power(self, name, action):
        """
        Change VM's power state
        :param name: str, virtual machine's name
        :param action: str, action to be performed (either start or stop)
        :return: bool, True if the result was successfull
        """
        if action not in ["start", "stop"]:
            raise OpenStackConnectorIntegrationTestSuiteException(f"The requested action {action} is incorrect. Must be either start or stop")
        
        logging.info(f"Received the power change request ({action}) for the virtual machine {name}")
        connection = self._openstack_connect()
        if action == "start":
            connection.vm_power(name, "on")
        else:
            connection.vm_power(name, "off")
        # Closing connection and deleting the openstacksdk instance to avoid timeout errors
        connection.close_connection()
        del connection
        logging.info(f"Power state of the virtual machine {name} was successfully changed")

        return True
    
    def change_vm_ram(self, name, ram):
        """
        Change VM's RAM amount
        :param name: str, virtual machine's name
        :param ram: int, RAM amount
        :return: bool, True if the result was successfull
        """
        logging.info(f"Received the RAM change request ({ram}) for the virtual machine {name}")
        connection = self._openstack_connect()
        connection.change_ram_qty(name, ram)
        # Closing connection and deleting the openstacksdk instance to avoid timeout errors
        connection.close_connection()
        del connection
        logging.info(f"The amount of RAM on the virtual machine {name} was successfully changed")

        return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="OpenStack Interface integration_test tool")
    parser.add_argument('-osurl', '--os_url', type=str,
                        help='OpenStack cloud URL', default=os.environ.get("OPENSTACK_URL") or None)
    parser.add_argument('-osusr', '--os_user', type=str,
                        help='OpenStack user', default=os.environ.get("OPENSTACK_USER") or None)
    parser.add_argument('-ospwd', '--os_password', type=str,
                        help='OpenStack password', default=os.environ.get("OPENSTACK_PASSWORD") or None)
    parser.add_argument('-osprjname', '--os_project_name', type=str,
                        help='OpenStack project name', default=os.environ.get("OPENSTACK_PROJECT_NAME") or "stands")
    parser.add_argument('-osprjdomname', '--os_project_domain_name', type=str,
                        help='OpenStack project domain name', default=os.environ.get("OPENSTACK_PROJECT_DOMAIN_NAME") or "company.com")
    parser.add_argument('-osusrdomname', '--os_user_domain_name', type=str,
                        help='OpenStack user domain name', default=os.environ.get("OPENSTACK_USER_DOMAIN_NAME") or "company.com")
    parser.add_argument('-osregname', '--os_region_name', type=str,
                        help='OpenStack region name', default=os.environ.get("OPENSTACK_USER_REGION_NAME") or "eu1")
    args = parser.parse_args()
    kwargs = dict(os_url=args.os_url, os_user=args.os_user, os_password=args.os_password, os_project_name=args.os_project_name,
                  os_project_domain_name=args.os_project_domain_name, os_user_domain_name=args.os_user_domain_name,
                  os_region_name=args.os_region_name)

    # Integration testing start
    integration_test_suite = OpenStackConnectorIntegrationTestSuite(**{key: value for key, value in kwargs.items() if value})
    integration_test_suite.vm_power("test-host", "start")
    integration_test_suite.vm_power("test-host", "stop")
    integration_test_suite.change_vm_ram("test-host", 7168)
    del integration_test_suite  
