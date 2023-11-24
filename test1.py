import math

from translator.conversor import find_value, get_decompacted_value

upper, ex_value, inc, mean, result, length = find_value(60)

decompacted = get_decompacted_value(upper, ex_value, inc, mean, length)
print(result)
print(decompacted)