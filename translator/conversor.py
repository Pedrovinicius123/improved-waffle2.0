from math import log2


def find_value(i, value):

    while True:

        num = (2**i)-value

        if num <= 0:
            pass

        else:
            result = log2(num)
            
            if result - round(result, 1) == 0:

                print(i)
                
                return result


        i += 1
