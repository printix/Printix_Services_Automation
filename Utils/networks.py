import requests
import logging
from Utils import ApiBaseFns

########################################################################################################################
# Network service test 
#######################
# Get list of Networks
# Get list of Netowork_ID's based on network name
# Add Network Name
# Add Network Gateway  - IP & MAC
# Modify Network IP & MAC
# Delete Network 
# Delete List of Networks
# Add Multiple Networks with same IP & different MAC
# Add Multiple Networks with same MAC & different IP
# Duplicate Networks
######################################################################################################################
def get_list_networks(**kwargs):
    '''List of users in tenant'''
    __network_names=[]
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
    #logging.info(resp.content)
    size=len(resp.json()['_embedded']['px:networkResources'])
    #logging.info(f"size of the response is: {size}")
    for i in range(size):
        if resp.json()['_embedded']['px:networkResources'][i]['name'] ==None:
            logging.error(f"empty project name from response body")
            raise TypeError
        else:
            #logging.info(f"Network Name {i} is: {resp.json()['_embedded']['px:networkResources'][i]['name']}")
            __network_names.append(resp.json()['_embedded']['px:networkResources'][i]['name'])
    #logging.info(__network_names)
    return __network_names

def add_network_Name(**kwargs):
    '''Add new network to Tenant -  name, ip & mac'''
    __network_id=None
    for key, value in kwargs.items():
        if key=="url":
            __url=value
        elif key=="Authorization":
            __auth_code=value
        elif key=="tenant_id":
            __tenant_id=value
        elif key=="network_name":
            __network_name=value
        else:
            logging.warning(f"Failed to validate network name: {value}")
            logging.info(f"key is{key}, value is {value}")
            TypeError
    __url=__url+"/"+__tenant_id+"/networks"
    __data = {'name': __network_name}
    resp=ApiBaseFns.postMethod(__url,__auth_code,__data)
    __network_id=resp.json()['_links']['px:discoverEnvironment']['href']
    __bef_network =__network_id.split("/networks/")[1]
    _after_network_id=__bef_network.split("/discoverEnvironment")[0]
    return _after_network_id

def delete_network(**kwargs):
    ''''Delete network'''
    __network_id_list=[]
    for key, value in kwargs.items():
        if key=="url":
            __url=value
        elif key=="Authorization":
            __auth_code=value
        elif key=="tenant_id":
            __tenant_id=value
        elif key=="__network_id":
            __network_id_list=value
        else:
            logging.warning(f"Failed to validate network name: {value}")
            logging.info(f"key is{key}, value is {value}")
            TypeError
        __size= len(__network_id_list)
        #map the network id to delete network
        logging.info(f"size of network id's list to delete: {__size}")
        for i in range(__size):
            if __network_id_list[i] ==None:
                logging.error(f"invalid network id from input list.")
                raise TypeError
            else:
                __url=__url+"/"+__tenant_id+"/networks/"+__network_id_list[i]
                #__url=__url+"/"+__tenant_id+"/networks/"+"71eaa2f0-5d24-40e8-ab26-4145cd74cbb9"
                resp=ApiBaseFns.deleteMethod(__url,__auth_code)
                assert resp.status_code ==200
        logging.info(f"End of delete_network method")

def get_list_network_ids(**kwargs):
    '''List of users in tenant'''
    __network_ids_list=[]
    __network_content=[]
    for key, value in kwargs.items():
        if key=="url":
            __url=value
        elif key=="Authorization":
            __auth_code=value
        elif key=="tenant_id":
            __tenant_id=value
        elif key=="network_name":
            __network_name=value
        else:
            logging.warning(f" unknown input in get list of networks: {value}")
            logging.info(f"key is{key}, value is {value}")
            TypeError
    __url=__url+"/"+__tenant_id+"/networks"
    resp=ApiBaseFns.getMethod(__url,__auth_code)
    #logging.info(f"network output: {resp.json()}")
    size=len(resp.json()['_embedded']['px:networkResources'])
    #logging.info(f"size of the response is: {size}")
    for i in range(size):
        if resp.json()['_embedded']['px:networkResources'][i]['name'] ==None:
            logging.error(f"empty project name from response body")
            raise TypeError
        else:
            #logging.info(f"Network Name {i} is: {resp.json()['_embedded']['px:networkResources'][i]['name']}")
            __network_content.append(resp.json()['_embedded']['px:networkResources'][i]['name'])
            __network_id=resp.json()['_embedded']['px:networkResources'][i]['_links']['px:discoverEnvironment']['href']
            __bef_network =__network_id.split("/networks/")[1]
            __after_network = __bef_network.split("/discoverEnvironment")[0]
            __outName=repr(resp.json()['_embedded']['px:networkResources'][i]['name'])[1:-1]
            if(str(__outName)==str(__network_name)):
                __network_ids_list.append(__after_network)
    #get network_id to the list __network_ids_list
    #logging.info(f"list of network id's: {__network_ids_list}")
    return __network_ids_list