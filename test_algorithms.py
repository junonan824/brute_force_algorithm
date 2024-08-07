from bfs import bfs
from brute_force import find_all_paths
from dfs import dfs
from graph_data import graph
from sequential_search import sequential_search

start_node = 'A'
end_node = 'F'
target_node = 'F'

# Test Brute Force
all_path = find_all_paths(graph=graph, start=start_node, end=end_node)
print('All Paths (Brute Force): ', all_path)

# Test sequential Search
is_found = sequential_search(graph=graph, start=start_node, target=target_node)

# Test bfs
print("BFS Traversal:")
bfs(graph=graph, start=start_node)
print()

# Test dfs
print("DFS Traversal:")
dfs(graph=graph, start=start_node)
print()
