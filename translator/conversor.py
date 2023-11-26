# With the help of 'Acervo Lima' and 'DelftStack' docs ;)
import decimal
from math import log2, ceil, log, floor
from time import sleep
import numpy as np
from sympy import isprime



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

        print('Power - value = ', value)

        ex_value = value 
        nums.append(value)


        if log2(value)%2 == 0:
            
            print(nums)

            print('UEPA')

            try: 
                upper = nums[len(nums)-2]

            except Exception as err0:
                print(f'OOB: {err0}')
                
                upper = nums[0]        

            final_result = {

                'upper' : upper,
                'ex_value' : ex_value,
                'processes' : inc,
                'mean' : return_mean_variation(powers),
                'result' : log2(nums[len(nums)-1]),
                'lower_power' : length

            }

            return final_result

        

        elif log2(value) - round(log2(value), 1) == 0 or nums.count(value) > 1:

            break

       

        print(nums)
        
                  
        inc += 1

    i = 0
    while True:
        i += 1

        val = 2**i

        print(val)
        
        result = 2**length-val

        print('Result: ',log2(result))

        sleep(1)

        if log2(result) - round(log2(result), 1) == 0 or result == ex_value:

            print('OPA!')

            print(nums)

            final_result = {

                'upper' : nums[len(nums)-2],
                'ex_value' : ex_value,
                'processes' : inc,
                'mean' : return_mean_variation(powers),
                'result' : log2(abs(result-2**length)),
                'lower_power' : length

            }
            return final_result

def get_decompacted_value(result):
    pass

    

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
    
