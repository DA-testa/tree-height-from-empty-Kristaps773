# 2218RDB518 Krists Kristaps Dūda
# python3

import sys
import threading

def compute_height(n, parents):
    children = [[] for i in range(n)]
    root = -1
    max_height = 0
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            children[parents[i]].append(i)
    stack = [(root, 1)]
    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)
        for child in children[node]:
            stack.append((child, height + 1))
    return max_height

def main():
    input1 = input()
    if 'F' in input1:
        file = input()
        file = "test/" + file
        if 'a' not in file:
            return
        with open(file, mode="r") as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    if 'I' in input1:
        n = int(input())
        parents = list(map(int, input().split()))
    print(compute_height(n, parents))
    
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
