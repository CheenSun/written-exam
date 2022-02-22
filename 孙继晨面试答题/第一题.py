#!/usr/bin/env python3

def new_reverse(s: str):
    s_list = list(s)
    if len(s) <= 1:
        return "".join(s)
    else:
        last = s_list.pop(-1)
        return last + new_reverse("".join(s_list))


def new_reverse_2(target: list):
    length = len(target)
    if length < 2:
        return target
    middle = int(length / 2)
    left = target[:middle]
    right = target[middle:]
    return new_reverse_2(right) + new_reverse_2(left)


if __name__ == "__main__":
    ss = "1234567"
    print(new_reverse(ss))
    print(new_reverse("789456122"))
    print("ok")

    print("".join(new_reverse_2(list("abcdefg"))))
    print("".join(new_reverse_2(list("123456789"))))
    print("".join(new_reverse_2(list("13265487"))))
