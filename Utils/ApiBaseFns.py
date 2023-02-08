import requests
import logging

def getMethod(url,auth_id):
    '''list the response from get method.'''
    resp= requests.get(url, headers =  {"Content-Type":"application/json", "Authorization": f"Bearer {auth_id}"}) 
    logging.info(resp.status_code)
    assert resp.status_code ==200
    return resp


def postMethod(url,auth_id,indata):
    '''list the response from get method.'''
    resp= requests.post(url, headers =  {"Content-Type":"application/json", "Authorization": f"Bearer {auth_id}"}, json=indata) 
    logging.info(resp.status_code)
    assert resp.status_code ==200
    return resp

def deleteMethod(url,auth_id):
    '''delete request'''
    resp= requests.delete(url, headers =  {"Content-Type":"application/json", "Authorization": f"Bearer {auth_id}"}) 
    logging.info(resp.status_code)
    assert resp.status_code ==200
    return resp