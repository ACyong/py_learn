# -*- coding: utf-8 -*-

from flask import jsonify

from fisher.helper import is_isbn_or_key
from fisher.yushu_book import YuShuBook

from . import web


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 普通关键字 or isbn
    :param page: 分页标识
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    return jsonify(result)
