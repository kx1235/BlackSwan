import json


def parse():
    with open("holdings_data.txt", 'r') as input:
        json.load(input)
