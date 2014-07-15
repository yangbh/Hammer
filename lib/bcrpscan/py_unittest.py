#!/usr/bin/env python
#coding=utf-8


"""
Run this script as:
    python -m pytest -v py_unittest.py
"""


from bcrpscan import test_get_parent_paths


def test_get_parent_paths():
    assert set(get_parent_paths('/a/b')) == set(['/', '/a/', '/a/b'])
    assert set(get_parent_paths('/a/b//')) == set(['/', '/a/', '/a/b/'])