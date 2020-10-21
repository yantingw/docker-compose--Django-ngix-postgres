import json
import numpy as np
import json
import base64

def decode_and_turn_json(d):
    b1 = d.encode("UTF-8")
    d = base64.b64decode(b1)
    s2 = d.decode("UTF-8")
    data = json.loads(s2)
    return data
    
    
def lambda_handler(event, context):
    # TODO implement
    d = event['body']
    data = decode_and_turn_json(d)
    
    org =np.array(data['img'])
    print(type(org))
    after = 255-org
    
    return {
        'statusCode': 200,
        'isBase64Encoded': False,
        'body': json.dumps({'new_data':after.tolist(),'name':"NICE!!!"})
    }
