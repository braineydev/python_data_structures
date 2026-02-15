
# non_linear_structures.py
# ----------------------------------------------------
# Demonstration of Non-Linear Data Structures in Python

# Non-Linear Data Structures:
# 1. Tree (Binary Tree)
# 2. Graph

# Includes:
# - Tree traversals (DFS: Inorder, Preorder, Postorder)
# - Graph traversal (BFS and DFS)
# - Time complexity explanations
# - Real-world applications

# Course: BIT2203 Data Structures & Algorithms


from collections import deque


# ==================================================
# 1. BINARY TREE IMPLEMENTATION
# ==================================================

class TreeNode:
    """
    Node class for Binary Tree.
    Each node contains:
    - data
    - left child
    - right child
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ==================================================
# TREE TRAVERSAL ALGORITHMS (DFS)
# ==================================================

def inorder_traversal(root):
    """
    Inorder Traversal (Left → Root → Right)
    Used in Binary Search Trees to get sorted order.
    Time Complexity: O(n)
    """
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)


def preorder_traversal(root):
    """
    Preorder Traversal (Root → Left → Right)
    Used in tree copying and expression trees.
    Time Complexity: O(n)
    """
    if root:
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    """
    Postorder Traversal (Left → Right → Root)
    Used in deleting trees and evaluating expressions.
    Time Complexity: O(n)
    """
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=" ")


# ==================================================
# 2. GRAPH IMPLEMENTATION (Adjacency List)
# ==================================================

class Graph:
    """
    Graph represented using Adjacency List.
    Suitable for sparse graphs.
    """

    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, vertex, edge):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
        self.adjacency_list[vertex].append(edge)

    # ------------------------------------------
    # Breadth First Search (BFS)
    # ------------------------------------------
    def bfs(self, start):
        """
        BFS Traversal
        Uses Queue (FIFO)
        Time Complexity: O(V + E)
        """
        visited = set()
        queue = deque([start])

        print("BFS Traversal:")

        while queue:
            vertex = queue.popleft()

            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                queue.extend(self.adjacency_list.get(vertex, []))

        print("\n")

    # ------------------------------------------
    # Depth First Search (DFS)
    # ------------------------------------------
    def dfs(self, start, visited=None):
        """
        DFS Traversal
        Uses recursion (Stack concept)
        Time Complexity: O(V + E)
        """
        if visited is None:
            visited = set()

        if start not in visited:
            print(start, end=" ")
            visited.add(start)

            for neighbor in self.adjacency_list.get(start, []):
                self.dfs(neighbor, visited)


# ==================================================
# MAIN EXECUTION
# ==================================================

if __name__ == "__main__":

    print("\nNON-LINEAR DATA STRUCTURES DEMONSTRATION")
    print("=" * 60)

    # ------------------------------------------
    # BINARY TREE DEMO
    # ------------------------------------------

    print("\nBINARY TREE DEMO")

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)

    print("Inorder Traversal:")
    inorder_traversal(root)
    print("\n")

    print("Preorder Traversal:")
    preorder_traversal(root)
    print("\n")

    print("Postorder Traversal:")
    postorder_traversal(root)
    print("\n")

    # ------------------------------------------
    # GRAPH DEMO
    # ------------------------------------------

    print("\nGRAPH DEMO")

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")
    graph.add_edge("D", "F")

    graph.bfs("A")

    print("DFS Traversal:")
    graph.dfs("A")
    print("\n")

    print("=" * 60)
