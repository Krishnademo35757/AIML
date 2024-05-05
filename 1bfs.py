from collections import deque

def bfs(graph, start):
  """
  Performs Breadth First Search on a graph represented by an adjacency list.

  Args:
      graph: A dictionary where the key is a node and the value is a list of its neighbors.
      start: The starting node for the BFS traversal.

  Returns:
      A list containing the nodes visited in BFS order.
  """
  visited = set()  # Keeps track of visited nodes
  queue = deque([start])  # Queue for BFS traversal

  while queue:
    node = queue.popleft()
    visited.add(node)
    print(node, end=" ")  # You can modify this to process the visited node

    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)

  return visited

# Example usage
graph = {
  0: [1, 2],
  1: [2, 3],
  2: [0, 1, 4],
  3: [1],
  4: [2]
}

bfs(graph, 0)  # Output: 0 1 2 3 4
