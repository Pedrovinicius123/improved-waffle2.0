from math import log2, ceil, log, floor
from time import sleep



def find_value(value):

    nums = []
    powers = []

    inc = 0

    while True:
        global ex_value
        
        length = len(bin(value)[2:])
        power = 2 ** length

        value = power-value      

        nums.append(value)
        powers.append(length)

        ex_value = value

        if log2(value) - round(log2(value), 1) == 0 or nums.count(value) > 1:
            break
                  
        inc += 1

    for i in range(length):
        val = 2**i
        
        result = log2(2**length-val)

        if result - round(result, 1) == 0:
            return ex_value, inc, return_mean_variation(powers), result

def get_decompacted_value(expo, val, alpha, processes):

    inc = expo

    for regression in range(processes):        

        inc += alpha

        value = 2**floor(inc)

        val = value - val 

    return val

def return_mean_variation(args:list):

    inc = 0
    prox = []

    for i in args:
        

        if args.index(i) == 0:
            inc = i

        else:

            inc = args[args.index(i)-1] - i

            prox.append(inc)

    variation = sum(prox)/len(prox)

    return variation
    
