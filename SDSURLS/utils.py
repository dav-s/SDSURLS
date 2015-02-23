import re

def to_hash(n):
    key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    r = n % 62
    n /= 62

    while n > 0:
        res = key[r] + res
        r = n % 62
        n /= 62

    res = key[r] + res
    return res


def fix_link(l):
    if re.match(r"[a-zA-z]+://.+", l):
        return l
    return "http://"+l
