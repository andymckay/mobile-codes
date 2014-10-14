# -*- coding: utf-8 -*-
import json
import os
from functools import partial
from collections import defaultdict, namedtuple

__all__ = ["countries"]


FILE_PATH = os.path.realpath(os.path.dirname(__file__))
COUNTRY_JSON_PATH = os.path.join(FILE_PATH, 'json', 'countries.json')
OPERATOR_JSON_PATH = os.path.join(FILE_PATH, 'json', 'operators.json')
COUNTRY_FIELDS = ('name', 'alpha2', 'alpha3', 'numeric', 'mcc')
OPERATOR_FIELDS = ('mcc', 'mnc', 'brand', 'operator')

Country = namedtuple('Country', COUNTRY_FIELDS)
Operator = namedtuple('Operator', OPERATOR_FIELDS)

_CACHE = {}


def _load_json(cache_key, json_path, wrapper):
    global _CACHE
    if cache_key not in _CACHE:
        with open(json_path, 'rb') as json_file:
            data = json.loads(json_file.read())
            _CACHE[cache_key] = [
                wrapper(*line) for line in data]
    return _CACHE[cache_key]


def _countries():
    return _load_json('countries_json', COUNTRY_JSON_PATH, Country)


def _operators():
    return _load_json('operators_json', OPERATOR_JSON_PATH, Operator)


def _build_index(idx, records):
    return dict((':'.join([r[k] for k in idx]).upper(), r) for r in records)


def _build_index_tuple(idx, records):
    # There can be multiple MCC codes per country
    # and there can be multiple countries for one MCC code
    result = defaultdict(list)
    for r in records:
        if isinstance(r[idx], list):
            for k in r[idx]:
                if k:
                    result[k.upper()].append(r)
        elif r[idx]:
            result[r[idx].upper()].append(r)
    return result


def _build_list_index(idx, records):
    res = defaultdict(list)
    for r in records:
        res[r[idx].upper()].append(r)
    return res


def _get(data, var, method, idx, *codes):
    global _CACHE
    if data.__name__ not in _CACHE:
        _CACHE[data.__name__] = data()
    if var not in _CACHE:
        _CACHE[var] = method(idx, _CACHE[data.__name__])
    return _CACHE[var][':'.join(k.upper() for k in codes)]


name = partial(_get, _countries, 'name', _build_index, [0])
alpha2 = partial(_get, _countries, 'alpha2', _build_index, [1])
alpha3 = partial(_get, _countries, 'alpha3', _build_index, [2])
numeric = partial(_get, _countries, 'numeric', _build_index, [3])
mcc = partial(_get, _countries, 'mcc', _build_index_tuple, 4)
operators = partial(_get, _operators, 'operators', _build_list_index, 0)
mcc_mnc = partial(_get, _operators, 'mcc_mnc', _build_index, [0, 1])
