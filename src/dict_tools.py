import collections
import functools
import operator

def combine_and_sum_dicts(dict_list: [dict]):
    """Combine dictionaries so that all items with same keys have their values summed"""
    #return dict(functools.reduce(operator.add, map(collections.Counter, dict_list)))
    return dict(functools.reduce(operator.add, (collections.Counter(d) for d in dict_list)))
