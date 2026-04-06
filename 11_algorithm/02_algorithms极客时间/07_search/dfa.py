# -*- coding: utf-8 -*-
import logging
import time


class DFAFilter(object):
    KEYWORD_CHAINS = {}  # 关键词链表
    DELIMIT = u'\x00'  # 结束符

    @classmethod
    def _add(cls, chars):
        """向关键词字典树添加关键词"""
        chars = chars.lower()

        level = cls.KEYWORD_CHAINS
        # 遍历关键字的每个字
        for char_index in range(len(chars)):
            # 如果这个字已经存在字符链的key中就进入其子字典
            if chars[char_index] in level:
                level = level[chars[char_index]]
            else:
                if not isinstance(level, dict):
                    break

                last_level = {}
                last_char = ''
                for sub_char_index in range(char_index, len(chars)):
                    level[chars[sub_char_index]] = {}
                    last_level, last_char = level, chars[sub_char_index]
                    level = level[chars[sub_char_index]]
                last_level[last_char] = {cls.DELIMIT: 0}
                break
        else:
            level[cls.DELIMIT] = 0

    @classmethod
    def _get(cls):
        """重写这个方法，获取需要查找的词"""
        return {"keywords": ["傻子", "坏人"]}

    @classmethod
    def _create(cls):
        """生成关键词字典树"""
        if cls.KEYWORD_CHAINS:  # 最好能加个缓存
            return
        begin = time.time()
        data = cls._get()
        label_keywords = data['keywords']
        for keyword in label_keywords:
            chars = keyword.strip()
            if not chars:
                continue
            cls._add(chars)
        logging.info("label_keywords create keywords_trie "
                     "elapsed time %s" % (time.time() - begin))

    @classmethod
    def _match(cls, start, content, level, keywords):
        """匹配关键字，返回本次匹配的步长"""
        step_ins = 0
        keyword = []
        for char in content[start:]:
            if char not in level:
                break

            keyword.append(char)
            if content[start:][step_ins] in level[char]:
                step_ins += 1
                level = level[char]
                continue
            step_ins += 1
            if cls.DELIMIT not in level[char]:
                level = level[char]
            else:
                if len(content[start:]) > step_ins and \
                        content[start:][step_ins] in level[char]:
                    level = level[char]
                    continue
                keywords.append(''.join(keyword))
                return step_ins
        if cls.DELIMIT in level:
            keywords.append(''.join(keyword))
        return 1

    @classmethod
    def find(cls, content):
        """查找所有的关键字"""
        if not content:
            return []
        begin = time.time()
        content = content.lower()
        cls._create()

        keywords = []
        level = cls.KEYWORD_CHAINS
        start = 0
        while start < len(content):
            step = cls._match(start, content, level, keywords)
            start += step
        logging.info("label_keywords find keywords "
                     "elapsed time %s" % (time.time() - begin))
        return keywords


if __name__ == "__main__":
    text = "你真是个大傻逼，大傻子，傻大个，大坏蛋，坏人。"
    result = DFAFilter.find(text)

    print(text)
    print(result)
