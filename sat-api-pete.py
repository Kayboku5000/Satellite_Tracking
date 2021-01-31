import requests
import json
from datetime import datetime

parameters = {
    "lat": -37.8077184,
    "lon": 144.9754624
}

response = requests.get("https://www.n2yo.com/rest/v1/satellite/radiopasses/33591/-37.7667/144.963/0/2/40/&apiKey=TBR2Z8-AGNNGB-Q6EB3P-4AIN")



def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())




#print(response.json())