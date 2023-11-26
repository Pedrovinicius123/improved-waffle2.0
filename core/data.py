from dataclasses import dataclass
from math import ceil
import os, pickle
from datetime import datetime, timedelta
from random import randint
import numpy as np
from time import sleep

@dataclass
class NullArray:
    nulls = None
    ones = None

@dataclass
class NullInstance(NullArray):

    instances: np.ndarray
    
    @classmethod
    def nulls(cls, instance):
        cls.nulls = instance

        return cls.nulls

    @classmethod
    def ones(cls, instance):
        cls.ones = instance

        return cls.ones
        

    def fill(self):

        count = 0
        
        inst = np.array([])


        for instance in self.instances:

            try:

                one = self.ones(instance[0])
                null = self.nulls(instance[1])

            except Exception as err0:
                print(f'What??? {err0}')

                self.ones = instance[0]
                self.nulls = instance[1]

                one, null = self.ones, self.nulls

            if count == 0:
                inst = np.append(self.instances, np.array([[one, null]]))

            else:
                inst = np.append(inst, np.array([one, null]))
                
            count += 1

        shape = inst.shape

        inst = inst[shape[0]//2:]

        print('Inst: ',inst)

        instances = {}

        counter = 0
        for index in range(len(inst.tolist())//2):
            
            instances[str(counter//2)] = inst[counter: counter+2]

            counter += 2

        print('Instans: ', instances)

        return instances


@dataclass
class Info(NullInstance):
    pass


@dataclass
class File(NullInstance):
    name: str
    creation: datetime
    sizeGB: float
    path: str

    def get_null_array(self):

        final_array = np.array([])    
        nulls_dict = self.fill()

        counter = 0
        for instances in nulls_dict.values():
        
            arr = [None for index in range(instances[0]+instances[1])]

            for index in range(instances[1]):

                try:
                    arr[index] = 1

                except Exception as err0:
                    print(f'OOB ({err0})')
                    break

                
            nulls_dict[str(counter)] = arr

            counter += 1


        return nulls_dict

    def generate_null_array(self, length):
        return np.array(['None' for l in range(length)])

    def compactate(self, value):        
        length = len(bin(value)[2:])
        null_array = self.generate_null_array(length)

        values, nulls = np.unique(null_array, return_counts=True)        
        alpha = nulls - 1 - 2**(length-1)

        delta = 2 ** length - value
        total = alpha - delta

        percentile = (length-1)**-1

        percentile_array = np.array([(percentile*inc) for inc in range(length-1)])
        print('Percentile: ', percentile_array)        

        for value in percentile_array:
            pass    

    def __repr__(self):
        return f'File {str} of {sizeGB} GB at {path}'


arr = np.array([[10, 2], [2, 10], [5, 3]])

file = File(arr, name='Petros.txt', creation=datetime(2023, 12, 26), sizeGB=25, path='path/to/file')
decompacted = file.get_null_array()

file.compactate(12)

print(decompacted)


