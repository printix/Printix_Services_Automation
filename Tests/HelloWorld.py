import logging
import pytest
import allure
import requests

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)
mylogger = logging.getLogger()


@allure.title("TESTCASE-T101-Get-API test")
@pytest.mark.order(1)
@pytest.mark.smoke
def testfns():
    resp=  requests.get("https://reqres.in/api/users?page=2")
    assert resp.status_code ==200
    mylogger.info('Get List of petids available')
    mylogger.warning('Get List of petids available1')

@allure.title("TESTCASE-T101-Get-API test")
@pytest.mark.order(1)
@pytest.mark.smoke
def testfns1():
    resp=  requests.get("https://reqres.in/api/users?page=2")
    assert resp.status_code ==200
    mylogger.info('Get List of petids available2')
    mylogger.warning('Get List of petids available3')
