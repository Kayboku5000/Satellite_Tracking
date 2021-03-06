import requests
import json
from datetime import datetime

parameters = {
    "lat": -37.8077184,
    "lon": 144.9754624
}

# response = requests.get("http://api.open-notify.org/astros.json")
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#jprint(response.json())

pass_times = response.json()['response']
#jprint(pass_times)

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

#print(risetimes)

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)