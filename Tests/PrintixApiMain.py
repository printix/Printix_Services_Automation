import logging
import pytest
import allure
from Utils import networks, workstations
from Utils.config_loader import load_service_devenv as devData
from Utils.config_loader import load_service_testenv as testData
import  Utils.Authorisation as auth
import Utils.users as tenantusers
import requests

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)
mylogger = logging.getLogger()
#Global variables Declaration
InEnvironment="dev"  # "dev" "test" "usdev"
__network_id=None
__auth01=__auth02=__auth03=None
if InEnvironment=="dev":
    __url=devData()['admin']['auth_url']
    __auth=devData()['admin']['auth_token_url']
    __username=devData()['admin']['username']
    __password=devData()['admin']['password']
    __env=devData()['admin']['environment']
    __tenantId=devData()['admin']['tenant_id']
elif InEnvironment=="test":
    __url=testData()['admin']['auth_url']
    __auth=testData()['admin']['auth_token_url']
    __username=testData()['admin']['username']
    __password=testData()['admin']['password']
    __env=testData()['admin']['environment']
    __tenantId=testData()['admin']['tenant_id']


@allure.title("TESTCASE-T100-Get-Printix-Authentication Code")
@allure.description("Test T100")
@pytest.mark.order(1)
@pytest.mark.smoke
@pytest.mark.regression
def testGetauthenticationCode():
    mylogger.info("input is: "+__url)
    authentication_code = auth.getauthcodefns(__auth,__env,__username,__password)
    mylogger.info("Authentication code: "+authentication_code)

@allure.title("TESTCASE-T101-Get-Tenant-Users-List")
@pytest.mark.order(2)
@pytest.mark.smoke
def testGetUsersList():
    authentication_code = auth.getauthcodefns(__auth,__env,__username,__password)
    mylogger.info("Authentication code: "+authentication_code)
    tenantusers.get_list_users(url=__url,Authorization=authentication_code,tenant_id=__tenantId)
    


@allure.title("TESTCASE-T102-Get-Tenant-Networks-List")
@pytest.mark.order(3)
@pytest.mark.smoke
def testGetNetworksList():
    authentication_code = auth.getauthcodefns(__auth,__env,__username,__password)
    mylogger.info("Authentication code: "+authentication_code)
    __network_names=networks.get_list_networks(url=__url,Authorization=authentication_code,tenant_id=__tenantId)
    logging.info(f"list of Netowrk names in tenant: {__network_names}")


@allure.title("TESTCASE-T103-Get-Tenant-Workstations-List")
@pytest.mark.order(4)
@pytest.mark.smoke
def testGetWorkstationsList():
    authentication_code = auth.getauthcodefns(__auth,__env,__username,__password)
    mylogger.info("Authentication code: "+authentication_code)
    workstations.get_list_workstations(url=__url,Authorization=authentication_code,tenant_id=__tenantId)

@allure.title("TESTCASE-T104-Get-Tenants-List")
@pytest.mark.order(5)
@pytest.mark.regression 
@pytest.mark.smoke
def testGetTenantsList():
    authentication_code = auth.getauthcodefns(__auth,__env,__username,__password)
    mylogger.info("Authentication code: "+authentication_code)
    workstations.get_list_workstations(url=__url,Authorization=authentication_code,tenant_id=__tenantId)

@allure.title("TESTCASE-T105-Add-Network-Name")
@pytest.mark.order(6)
@pytest.mark.bugfix
def testAddNetworkName():
    authentication_code = auth.getauthcodefns(__auth,__env,__username,__password)
    mylogger.info("Authentication code: "+authentication_code)
    #add network name   =  "Kofax_Network_Date_Random number"
    __network_id=networks.add_network_Name(url=__url,Authorization=authentication_code,tenant_id=__tenantId,network_name="printix_nt_dk_herlev_080223")
    logging.info(f"netowrk id is added : {__network_id}")


@allure.title("TESTCASE-T10X-delete-Network")
@pytest.mark.order(6)
@pytest.mark.smoke
def testDeleteNetwork():
    authentication_code = auth.getauthcodefns(__auth,__env,__username,__password)
    mylogger.info("Authentication code: "+authentication_code)
    #add network 
    networks.add_network_Name(url=__url,Authorization=authentication_code,tenant_id=__tenantId,network_name="1a1")
    #fetch network id based on network name
    __network_id_list=networks.get_list_network_ids(url=__url,Authorization=authentication_code,tenant_id=__tenantId,network_name="1a1")
    logging.info(__network_id)
    #delete network based on ID or ID's.
    #networks.delete_network(url=__url,Authorization=authentication_code,tenant_id=__tenantId,network_name="printix_nt_dk_herlev_080223")

