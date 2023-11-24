import math

from translator.conversor import find_value, get_decompacted_value

upper, ex_value, processes, mean, result, length= find_value(365)



decompacted = get_decompacted_value(upper, processes=processes, alpha=mean, expo=length, val=ex_value)

print(upper)

print(mean, processes)

print(result, processes)

print(decompacted)
