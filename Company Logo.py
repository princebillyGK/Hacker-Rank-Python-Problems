import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()
    
    count_map = {}
    
    for i in s:
        count_map[i] = count_map.get(i, 0) + 1
    
    count_pairs = sorted(count_map.items())
    count_pairs = sorted(count_pairs, key=lambda pair: pair[1], reverse=True)
    
    for i in range(3):
        print(count_pairs[i][0], count_pairs[i][1])
