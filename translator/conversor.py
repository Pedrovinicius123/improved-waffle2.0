# With the help of 'Acervo Lima' and 'DelftStack' docs ;)
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

        if log2(value) - round(log2(value), 1) == 0 or nums.count(value) > 1:

            break

        nums.append(value)

        ex_value = value
        
                  
        inc += 1

    for i in range(length):
        val = 2**i
        
        result = 2**length-val

        if result == ex_value:

            print(nums)

            return nums[len(nums)-2], ex_value, inc, return_mean_variation(powers), log2(abs(result-2**length)), length

def get_decompacted_value(upper, expo, val, alpha, processes):

    counter = 0
    static_expo = upper

    print('static_expo, ',static_expo)

    print('pre-expo: ', expo)

    expo = floor(log2(expo+2**expo))

    print('post-expo: ', expo)

    print(static_expo)

    if processes == 1:
        return 2**floor(expo+alpha) - upper


    zeros_array = np.array([])
    ones_array = np.array([])
    total_array = np.array([])
    regression_array = np.array([])    

    
    for index in range(processes):

        validation = expo + floor(alpha*index)

        if index == 0:
            pass

        else:

            zeros_array = np.append(zeros_array, floor(validation))
            ones_array = np.append(ones_array, floor(validation+1))

    total_array = np.append(total_array, np.concatenate((zeros_array, ones_array)))
    num, counts = np.unique(np.sort(total_array), return_counts=True)

    result_array = np.column_stack((num, counts))

    print(result_array, ' Result array')

    for pre_regression in range(processes):

        value = result_array[pre_regression]

        if value[1] > 1:
            counter += 1

            if counter >= 2:
                pass

            elif counter == 1:
                major = value

            else:
                major = value if value > major else major


        else:
            regression_array = np.append(regression_array, value[0])

    counter = 0

    print('Pre regression arr: ', regression_array)

    for value in regression_array:

        regression_array[counter] = floor(expo*alpha) + value
        counter += 1

    print('Regression arr: ',regression_array)

    for regression in range(processes):

        try:

            print(regression)
        
            print('Exponential, ',expo)
            
            value = 2**regression_array[regression]
            
            static_expo = value - static_expo
            val = static_expo

            print(val)  

            sleep(1)


        except Exception as err:
            print('Array index out of bounds, continue process...')
            break

     

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
    
