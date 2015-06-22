#!/usr/bin/env python
# __author__ = 'aaron'

def dict_to_adj(d):
    adj = []
    # Add a list for each person in the list
    for x in d:
        adj.append(list())
        # Add a zero for each available edge
        for y in range(len(d)):
            adj[-1].append(0)

    for x in d:
       for val in d[x]:
        adj[x][val] = 1
    return adj

def nodes_of_degree(d, n):
    adj = dict_to_adj(d)
    numNode, list = 0, []
    for singleEdges in adj:
        num = 0
        for edge in singleEdges:
            if edge != 0:
                num = num + 1
        if num == n:
            list.append(numNode)
        numNode = numNode + 1
    return list
#
# d = {0: [1,2], 1: [0], 2: [], 3: [], 4: [3, 2, 4], 5: [1, 2, 3, 4,], 6:[5, 7], 7: [6]}
# n = 0
# for x in nodes_of_degree(d, n):
#     print(x)