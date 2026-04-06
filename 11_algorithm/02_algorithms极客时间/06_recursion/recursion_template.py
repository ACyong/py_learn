"""
1. 不要人肉递归
2. 找到最近重复子问题
3. 数学归纳法思维
"""


def recursion(level, *args, **kwargs):
    # 递归终止条件
    if level > MAX_LEVEL:  # NOQA
        process_result  # NOQA
        return

    # 处理当前层逻辑
    process(level, data)  # NOQA

    # 下探到下一层
    recursion(level+1, *args, **kwargs)

    # 清理当前层(如果需要)
