import requests
import json
from datetime import datetime




response = requests.get("https://www.n2yo.com/rest/v1/satellite/above/-37.8077184/144.9754624/0/70/18/&apiKey=TBR2Z8-AGNNGB-Q6EB3P-4AIN")






def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
