# -*- coding: utf-8 -*-

from http import HTTP


class YuShuBook(object):
    ISBN_URL = 'http://t.yushu.im/v2/book/isbn/{}'
    KEYWORD_URL = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.ISBN_URL.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword):
        url = cls.KEYWORD_URL.format(keyword)
        result = HTTP.get(url)
        return result
