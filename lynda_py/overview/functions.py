#!/usr/bin/env python3


def function(n=1, m='test'):  # n and m are default arguments
    print(n, m)
    return n * 2


function()
x = function(100, "hello")
print(x)
