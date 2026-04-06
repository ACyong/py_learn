visited = set()


# 递归写法
def dfs(node, visited):  # NOQA
    if node in visited:  # terminator
        # already visited
        return
    visited.add(node)
    # process current node here. 	...
    for next_node in node.children():
        if next_node not in visited:
            dfs(next_node, visited)


# 非递归写法
def dfs(self, root):  # NOQA
    if tree.root is None:  # NOQA
        return []
    visited, stack = [], [root]  # NOQA
    while stack:
        node = stack.pop()
        visited.add(node)  # NOQA
        process(node)  # NOQA
        # 生成相关的节点
        nodes = generate_related_nodes(node)  # NOQA
        stack.push(nodes)  # NOQA

    # other processing work
