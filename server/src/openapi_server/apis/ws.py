from websocket import create_connection
import socket
from openapi_server.models.resource import Resource
import json

def _getConnectionStatus(IP):
    try:
        host = socket.gethostbyname(IP)
        socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False


def ws_command(IP,GTP_ADDR,resource):
    print("WS.....")
    if not _getConnectionStatus(IP):
        return("Connection failed")
    soft_action=None
    soft_action_params=None
    for af in resource.activation_feature:
        for af_fc in af.feature_characteristic: 
            #print(af_fc)
           # print(af_fc.name)
            if af_fc.name=="soft_action":
                # print(af_fc.name)
                # print(af_fc.value["value"])
                soft_action=af_fc.value["value"]["command"]
                if "parameters" in af_fc.value["value"]:
                    soft_action_params=af_fc.value["value"]["parameters"]
    
    cmd_json=dict()
    cmd_json["message"]=soft_action
    
    #status of connections    
    if soft_action=="status":
        soft_action="ng"
        cmd_json["message"]=soft_action

    #delete amf     
    if soft_action=="delete":
        cmd_json["message"]="ngdelete"
        cmd_json["addr"]=soft_action_params

    #add amf     
    if soft_action=="add":
        cmd_json["message"]="ngadd"
        cmd_json["amf_addr"]=soft_action_params
        cmd_json["gtp_ext_addr"]=GTP_ADDR
        cmd_json["ngap_bind_addr"]=GTP_ADDR

    #connect to amf     
    if soft_action=="connect":
        cmd_json["message"]="ngconnect"
        if (soft_action_params):
            cmd_json["address"]=soft_action_params

    #disconnect from amf     
    if soft_action=="disconnect":
        cmd_json["message"]="ngdisconnect"
        if (soft_action_params):
            cmd_json["address"]=soft_action_params


    try:
        #have port as parameter only default at the moment
        ws = create_connection("ws://"+IP+":9001/")
        # cmd="".join(["{\"message\": \"",soft_action,"\"}"])
        # print(cmd)
        print(json.dumps(cmd_json))
        ws.send(json.dumps(cmd_json))
        #Get the first respo that everything is OK
        result =  ws.recv()
        #Get the actual response OK
        result =  ws.recv()
        ws.close()
        res_json = json.loads(result)
        #data={"cmd":res_json["message"],"output":res_json["messages"]}

    except Exception as e:
        print(repr(e))
        return("WS connection failed")
    
    return res_json