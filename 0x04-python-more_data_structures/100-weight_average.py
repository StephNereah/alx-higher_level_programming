#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_p = sum(score * weight for score, weight in my_list)
    sum_w = sum(weight for _, weight in my_list)

    return sum_p / sum_w
