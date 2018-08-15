
"""

用from allattr import *
"""
__all__ = ["hello", "name1"]

def hello():
    pass

def _hello(): # 此函数将在from import * 语句中不被导入
    pass

def __hello():
    pass

name = "aaa"
name1 = "bbbb"