#!/usr/bin/env python3
import json


def get_children(current, root_val):
    data = []
    for one in current:
        if one["code"] == root_val:
            one["children"] = get_children(current, one["code"])
            data.append(one)
    return data

if __name__ == '__main__':
    with open('./2.json', 'r') as f:
        data = json.load(f)
        print(get_children(data, ""))
