#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    len_s = len(s)
    print('len',len_s)
    max_mid = len_s // 2
    flag_mid = 1 if len_s % 2 == 0 else 0
    for i in range(max_mid):
        left_pos = i
        right_pos = len_s - i - 1
        
        left_value = s[left_pos]
        right_value = s[right_pos]
        if left_value == right_value:
            continue
        else:
            #check if it's the middle and both values are different
            print('->',left_pos,' - ',right_pos)
            print('Values:',left_value,',',right_value)
            if i == max_mid - 1:
                return i
            else: 
                # check of we have to take the left or right value
                print('flagmid',flag_mid)
                print(s[left_pos  + 1 : max_mid + 1])
                print(s[max_mid + 1 + flag_mid: right_pos + 1][::-1])
                if s[left_pos  + 1 : max_mid + 1] == s[max_mid + 1 + flag_mid: right_pos + 1][::-1]:
                    return left_pos
                else:
                    return right_pos
    return -1

if __name__ == '__main__':
    input_file = sys.argv[1]
    f_lines = open(input_file, "r").readlines()

    q = int(f_lines[0])

    for q_itr in range(q):
        s = f_lines[q_itr + 1].strip()

        result = palindromeIndex(s)

        print(f'Resultado final para {q_itr + 1}° caso -> {result}')
