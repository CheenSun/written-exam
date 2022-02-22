#!/usr/bin/env python3

def marge(a, b):
    result = []
    point_a, point_b = 0, 0
    while point_a < len(a) and point_b < len(b):
        # if not (point_a < len(a) and point_b < len(b)):
        #     break
        if a[point_a] < b[point_b]:
            result.append(a[point_a])
            point_a += 1
        else:
            result.append(b[point_b])
            point_b += 1
    # 如果是a数组越界
    if point_a >= len(a):
        # 就把剩余的b数组加入结果
        result += b[point_b:]
    # 如果是b数组越界
    if point_b >= len(b):
        result += a[point_a:]
    return result


def sort(target: list):
    length = len(target)
    if length == 1:
        return target
    else:
        middle = int(length / 2)
        # 对切割出的数组排序
        left = sort(target[:middle])
        right = sort(target[middle:])
        # 合并两个有序数组
        return marge(left, right)


if __name__ == '__main__':
    print(sort([4, 3,2]))
    print((sort([3, 1, 4, 1, 5, 9, 2, 6, 5])))
    print((sort([3, 1, 4, 1, 5, 9, 2, 6])))
