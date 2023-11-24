# With the help of 'Acervo Lima' and 'DelftStack' docs ;)
import decimal
from math import log2, ceil, log, floor
from time import sleep
import numpy as np



def find_value(value):

    nums = []
    powers = []



    inc = 0

    while True:
        global ex_value
        
        length = len(bin(value)[2:])
        power = 2 ** length

        value = power-value

        powers.append(length) 

        ex_value = value 

        nums.append(value)


        if log2(value)%2 == 0:
            
            print(nums)

            return nums[0], ex_value, inc, power, log2(abs(value-2**length)), length

        

        elif log2(value) - round(log2(value), 1) == 0 or nums.count(value) > 1:

            break

       

        print(nums)
        
                  
        inc += 1

    for i in range(length):
        val = 2**i

        print(val)
        
        result = 2**length-val

        if result == ex_value:

            print(nums)

            return nums[len(nums)-2], ex_value, inc, return_mean_variation(powers), log2(abs(result-2**length)), length

def get_decompacted_value(nums, ex_value, inc, mean, length):

    #Developement of the core of the decompact function

    import numpy as np

    ones_array = np.array([])
    zeros_array = np.array([])
    total_array = np.array([])

    if inc == 0:
        return mean - nums

    for pre_processing in range(inc):
        
        

         ones_array = np.append(ones_array, )

    

def return_mean_variation(args:list):

    inc = 0
    prox = []

    for i in args:
        

        if args.index(i) == 0:
            inc = i

            

        else:

            inc = args[args.index(i)-1] - i

            prox.append(inc)

    print('Prox: ',prox)

    try:

        variation = sum(prox)/len(prox)

    except Exception:
        print(':D')

    else:
        return variation
    
