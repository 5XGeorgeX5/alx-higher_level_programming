#!/usr/bin/python3
"""Defines pascal_triangle function."""


def pascal_triangle(n):
    """returns Pascal's triangle of n rows"""
    ans = []
    if n <= 0:
        return ans
    ans.append([1])
    for i in range(1, n):
        lst = [1]
        for j in range(1, (i + 1) // 2):
            lst.append(ans[i - 1][j] + ans[i - 1][j - 1])
        lst2 = lst.copy()
        lst2.reverse()
        if i % 2 == 0:
            lst.append(ans[i - 1][i // 2] * 2)
        lst = lst + lst2
        ans.append(lst)
    return ans
