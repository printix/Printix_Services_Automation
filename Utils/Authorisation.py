import yaml
import logging
import requests     
import json     
from Utils.config_loader import load_service_devenv as devData
from Utils.config_loader import load_service_testenv as testData
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)
mylogger = logging.getLogger()

#Global variables Declaration

__auth01=__auth02=__auth03=None
__code= None
__grant_type= devData()['admin']['grant_type']
__redirect_uri= devData()['admin']['redirect_uri']   
__client_id= devData()['admin']['client_id']   
__client_secret= devData()['admin']['client_secret']
__env= devData()['admin']['environment']

def getauthcodefns(url,env,username,password):
    resp= requests.get(url, allow_redirects=False)
    assert resp.status_code ==302
    __auth01_resp = resp.headers.get('Location').split('&jwt')
    #mylogger.info("first auth01:"+__auth01[1])
    __auth01= __auth01_resp[1]
    __auth02url ="https://auth."+env+".printix.net/login?jwt"+str(__auth01)+"&username="+username+"&password="+password
    __code=getCodeAuthfn(__auth02url)
    return  __code

def getCodeAuthfn(url1):
    resp=  requests.post(url1, allow_redirects=False)
    assert resp.status_code ==302
    __Auth02 = resp.headers.get('Location')
    #mylogger.info("second auth02:"+__Auth02)
    auth03_resp=requests.get(str(__Auth02), allow_redirects=False)
    assert auth03_resp.status_code ==302
    __Auth03=auth03_resp.headers.get('Location')
    __auth03_01_out= __Auth03.split('?')
    __auth03_01_out=__auth03_01_out[1].split('&')[0]
    __Auth03=__auth03_01_out.split('=')[1]
    __code=__Auth03
    #mylogger.info("Code :"+__code)
    __auth_url="https://auth."+__env+".printix.net/oauth/token"
    __authorisation_code= requests.post(__auth_url,data={'grant_type': {__grant_type},'code': {__code},'redirect_uri': {__redirect_uri},'client_id': {__client_id},'client_secret': {__client_secret}})
    assert __authorisation_code.status_code ==200
    return str(__authorisation_code.json()['access_token'])


