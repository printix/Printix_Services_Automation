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
InEnvironment="test"  # "test" "test" "usdev"
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
@pytest.mark.suneetha
def testGetauthenticationCode():
    mylogger.info("input is: "+__url)
    authentication_code = auth.getauthcodefns(__auth,__env,__username,__password)
    mylogger.info("Authentication code: "+authentication_code)

