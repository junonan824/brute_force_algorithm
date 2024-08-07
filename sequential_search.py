def sequential_search(graph, start, target):
    for node in graph[start]:
        if node == target:
            return True
    return False