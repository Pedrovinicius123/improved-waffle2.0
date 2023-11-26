import math

from translator.conversor import find_value, get_decompacted_value

result = find_value(978)

print('Processes: ',  result['processes'])

decompacted = get_decompacted_value(result)
print(result)
print(decompacted)