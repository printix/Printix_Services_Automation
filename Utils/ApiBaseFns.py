import requests
import logging

def getMethod(url,auth_id):
    '''list the response from get method.'''
    resp= requests.get(url, headers =  {"Content-Type":"application/json", "Authorization": f"Bearer {auth_id}"}) 
    assert resp.status_code ==200
    return resp


