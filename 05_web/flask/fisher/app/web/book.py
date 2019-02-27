# -*- coding: utf-8 -*-

from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook


@app.route('/book/search/<p>/<page>')
def search(q, page):
    """
    q: 普通关键字 or isbn
    page: 分页标识
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    return jsonify(result)
