def bds(root):
    visited = set()
    queue = []  # NOQA
    queue.append([root])

    while queue:
        node = queue.pop()
        visited.add(node)
        process(node)  # NOQA
        nodes = generate_relaed_nodes(node)  # NOQA
        queue.push(nodes)  # NOQA

    # other precessing work
