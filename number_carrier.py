import json
import requests
from keys import APItoken as get_key
# You may need to install Requests pip
# python -m pip install requests



def phone_carrier(phone):
    
    if len(phone) == 10:
        respData = requests.get(
            url=f'https://api.apilayer.com/number_verification/validate?number=1{phone}', 
            headers={
                "apikey": get_key.api_layer_key
            }
        )
        
    validator = respData.json()
    
    # Check to see if our query was successful.
    print(validator)
    if validator["valid"] and validator['valid'] == True:
       
        return {
            "status": "success", 
            "results": 
                {
                    "carrier": validator["carrier"],
                    "line_type": validator["line_type"]
                }
        }
    else:
        return {"status": "failed", "results": "remove"}