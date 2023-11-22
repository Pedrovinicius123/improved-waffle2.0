import math
from translator.conversor import find_value, get_decompacted_value

result, processes, mean, power = find_value(1000)

print('Processes: ', processes)
print('Compacted: ', power)
print('Mean: ', mean)

value = get_decompacted_value(expo=power+1, processes=processes, val=result, alpha=mean)

print('Input value: ', value)
