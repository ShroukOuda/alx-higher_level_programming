#!/usr/bin/python3
def remove_char_at(s, n):
    if n >= 0:
        return (s[:n] + s[n+1:])
    else:
        return (s[:n] + s[len(s) + n + 1:])
