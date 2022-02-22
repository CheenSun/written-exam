#!/usr/bin/env python3
import json
import operator


def make_tree(current, root_val):
    data = []
    for one in current:
        if one["parent"] == root_val:
            one["children"] = make_tree(current, one["code"])
            data.append(one)
    return data


def flattening(data: list[dict]):
    returned = []
    for one in data:
        children = one.pop("children")
        returned.append(one)
        if children is not None:
            children = flattening(children)
            returned = returned + children
    return returned


if __name__ == '__main__':
    with open('./2.json', 'r') as f:
        data = json.load(f)
        tree = make_tree(data, "")
        print(tree)
        flatted = flattening(tree)
        print(flatted)

        sorted_data = sorted(data, key=operator.itemgetter('id'))
        sorted_flatted = sorted(flatted, key=operator.itemgetter('id'))

        if sorted_data == sorted_flatted:
            print("Yes, I did it")
