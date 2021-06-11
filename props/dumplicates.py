
import json

with open("all-properties.en.json") as f:
	props = json.load(f)

recommended = [prop for prop in props if prop["status"] == "REC"]

for idx, val in enumerate(recommended):
	print(f"\t{idx}. {val}")

