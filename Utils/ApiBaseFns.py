import requests
import logging

def getMethod(url,auth_id):
    '''list the response from get method.'''
    resp= requests.get(url, headers =  {"Content-Type":"application/json", "Authorization": f"Bearer {auth_id}"}) 
    logging.info(f"status of Get Method: {resp.status_code}")
    assert resp.status_code ==200
    return resp


def postMethod(url,auth_id,indata):
    '''list the response from get method.'''
    resp= requests.post(url, headers =  {"Content-Type":"application/json", "Authorization": f"Bearer {auth_id}"}, json=indata) 
    logging.info(f"status of Post Method: {resp.status_code}")
    assert resp.status_code ==200
    return resp

def deleteMethod(url,auth_id):
    '''delete request'''
    resp= requests.delete(url, headers =  {"Content-Type":"application/json", "Authorization": f"Bearer {auth_id}"}) 
    logging.info(f"status of Delete url: {url} & status code : {resp.status_code}")
    return resp

def putMethod():
    '''update the existing data'''