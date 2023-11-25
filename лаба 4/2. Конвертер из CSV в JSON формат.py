import json


def func() -> float:
    file = "input.json"
    with open(file) as f:
        json_data = json.load(f)
    sum_values = sum([item["score"] * item["weight"] for item in json_data])
    return round(sum_values, 3)


print(func())
