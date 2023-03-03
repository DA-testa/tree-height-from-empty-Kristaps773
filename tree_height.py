# 2218RDB518 Krists Kristaps Dūda
# python3

import sys
import threading


def compute_height(n, parents):
    koks = {}
    root = -1
    max_height = 0
    for i in range(n):
        koks[i] = []
    for i in range(n):
        if parents[i] is -1:
            root = i
        else:
            koks[parents[i]].append(i)
    stack = [(root,1)]
    while stack:
        node,height = stack.pop()
        max_height = max(max_height,height)
        for child in koks[node]:
            stack.append((child,height+1))
    return max_height
    


def main():
    input1 = input()

    if 'F' in input1:
        file = input()
        file = "test/" + file
        with open(file, mode = "r") as f:
            if 'a' not in file:
                return
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    elif 'I' in input1:
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        return

    print(compute_height(n, parents))
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()


