import requests
import logging
from Utils import ApiBaseFns

def get_list_networks(**kwargs):
    '''List of users in tenant'''
    for key, value in kwargs.items():
        if key=="url":
            __url=value
        elif key=="Authorization":
            __auth_code=value
        elif key=="tenant_id":
            __tenant_id=value
        else:
            logging.warning(f" unknown input in get list of networks: {value}")
            logging.info(f"key is{key}, value is {value}")
            TypeError
    __url=__url+"/"+__tenant_id+"/networks"
    resp=ApiBaseFns.getMethod(__url,__auth_code)
    logging.info(resp.content)
