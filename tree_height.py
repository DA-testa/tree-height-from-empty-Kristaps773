# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    max_height = 0
    heights = [0] * n
    # Your code here

    for i in range(n):
        heigth = 0
        j = i 
        while j != -1:
            if heights[j] != 0:
                height += heights[j]
                break
            height += 1
            j = parents[j]
        heights[i] = heigth
        max_height = max(max_height,heigth)
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

