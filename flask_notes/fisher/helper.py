# -*- coding: utf-8 -*-

def is_isbn_or_key(word):
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    elif '-' in q:
        short_q = q.replace('-', '')
        if len(short_q) == 10 and short_q.isdigit():
            isbn_or_key = 'isbn'