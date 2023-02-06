import logging
import pytest
import allure
from Utils.config_loader import load_service_devenv as devData
import  Utils.Authorisation as auth
import requests

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)
mylogger = logging.getLogger()
#Global variables Declaration
__auth=devData()['admin']['auth_token_url']
__username=devData()['admin']['username']
__password=devData()['admin']['password']
__auth01=__auth02=__auth03=None
__env=devData()['admin']['environment']
@allure.title("TESTCASE-T101-Get-Printix-Authentication Code")
@pytest.mark.order(1)
@pytest.mark.smoke
def testGetauthenticationCode():
    authentication_code = auth.getauthcodefns(__auth,__env,__username,__password)
    mylogger.info("Authentication code: "+authentication_code)
