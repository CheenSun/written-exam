#!/usr/bin/env python3
import json

if __name__ == '__main__':
    with open('./1.json', 'r') as f:
        data = json.load(f)
        data_dict = dict()
        for one in data:
            data_dict[one["serial"]] = one
        new_data = list()
        for key, val in data_dict.items():
            new_data.append(val)
        print(new_data)
