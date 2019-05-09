# -*- coding: utf-8 -*-


def is_isbn_or_key(word):
    """判断查询关键字的类型

    :param word: 查询关键字
    :return: 关键字的类型
    """
    # isbn13 是由13个0-9 的数字组成，isbn10 是由10个0-9或'_'的数字组成。
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    elif '-' in word:
        short_word = word.replace('-', '')
        if len(short_word) == 10 and short_word.isdigit():
            isbn_or_key = 'isbn'

    return isbn_or_key
