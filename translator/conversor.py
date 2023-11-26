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

    #Developement of the core of the decompact function

    import numpy as np

    ones_array = np.array([])
    zeros_array = np.array([])
    total_array = np.array([])

    if result['processes'] == 0:
        return abs(2 ** result['lower_power'] - result['upper'])

    for pre_processing in range(result['processes']):

        value = floor(result['lower_power'] + result['mean'] * pre_processing)

        print('Value, initial: ',value)

        ones_array = np.append(ones_array, value+1)
        zeros_array = np.append(zeros_array, value)
    
    ones_array = np.delete(ones_array, 0)
    zeros_array = np.delete(zeros_array, 0)

    print(zeros_array)

    total_array = np.concatenate((ones_array, zeros_array))
    print(total_array)
    
    nums, counts= np.unique(total_array, return_counts=True)
    result_array = np.column_stack((nums, counts))

    print(result_array)
    
    counter = 0
    total_array = np.array([])

    for processing in range(result['processes']):

        if result['processes'] == 1:
            
            value = result['upper']

        else:

            value = result_array[processing]

            if value[1] > 1:

                counter += 1

                if counter == 1:
                    pass

                else:
                    total_array = np.append(total_array, value[0])

            else:
                total_array = np.append(total_array, value[0])

    
    upper = result['upper']
    lower = result['lower_power']
    mean = result['mean']
    ex_value = result['ex_value']

    print(ex_value)

    counter = 0

    print(total_array) 
        
    for value in total_array:
        print(value)
        total_array[counter] = floor(2 * mean + value) 

        counter += 1

    print('Post, ', total_array)

    value = upper + ex_value*2

    print('Value, pre regression: ', value)

    for regression in range(result['processes']):
        try:

            sleep(1)
            print(value)

            value = floor(2 ** total_array[regression] - value)

            response = value

        except Exception as err0:
            print(f'OOB ({err0}), continue process...')

    if result['processes'] == 1:
        response = len(bin(upper)[2:])
        return 2**(response+result['mean']) - upper

    return response          

    

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
    
