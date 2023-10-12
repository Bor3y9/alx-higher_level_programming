#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        suma = 0
        sumw = 0
        for i, j in my_list:
            suma += (i * j)
            sumw += j
            avg = suma / sumw
        return avg
    return 0
