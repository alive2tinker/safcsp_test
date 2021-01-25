import json
import random

with open('data.json', 'r') as jFile:
    jData = json.load(jFile)
    index = random.randint(0, len(jData))
    print(jData['data'][index])