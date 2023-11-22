from math import log2, ceil, log, floor
from time import sleep



def find_value(value):

    nums = []
    inc = 0

    while True:
        
        length = len(bin(value)[2:])
        power = 2 ** length

        value = power-value      

        nums.append(value)

        if log2(value) - round(log2(value), 1) == 0 or nums.count(value) > 1:
            break

        inc += 1

    for i in range(length):
        val = 2**i
        
        result = log2(2**length-val) 

        if result - round(result, 1) == 0:
            return log2(val), inc, length

def get_decompacted_value(value, processes):
    for regression in range(processes):
        
