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
    # implement input form keyboard and from files
    input1 = input()
        
    if 'F' in input1:
        file = input()
        file = "test/" + file
        try:
            with open(file, "r") as f:
                if 'a' not in file:
                    return
                n = int(f.readline())
                parent = list(map(int, f.readline().split()))
        except FileNotFoundError:
            return
        
    elif 'I' in input1:
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        return
     

    

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    # n = int(input("n"))
    # parents = int(input("parents"))
    print(compute_height(n,parents))
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
