#!/usr/bin/env python3
import json
with open('ex5.json', 'r') as file:
    d = json.load(file)

for data in d:
    if data["name"] == "Old Fashioned" and i["type"] == "donut": 
        data["batters"]["batter"].append({"id": "1008", "type": "Tea"})
        break

with open('ex5.json', 'w') as w:
    json.dump(d, w, indent=2)
