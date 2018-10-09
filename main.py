import os
import json
import pandas as pd

path = "data/2017_09_26"

files = [f for f in os.listdir(
    path) if f.endswith(".json")]
print(files)

data = []

with open("data/2017_09_26/2017_09_26_00_06.json") as f:
    for line in f:
        data.append(json.loads(line))

print(data)
