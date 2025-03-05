import collections
import functools
import operator

def combine_and_sum_dicts(dict_list: [dict]):
    """Combine dictionaries so that all items with same keys have their values summed"""
    combined = collections.defaultdict(int)
    for d in dict_list:
        for key, value in d.items():
            combined[key] += value
    return dict(combined)