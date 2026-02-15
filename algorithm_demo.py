
# algorithms_demo.py
# -------------------------------------------------------
# Demonstration of Algorithms Operating on Data Structures

# Includes:
# 1. Linear Search
# 2. Binary Search
# 3. Bubble Sort
# 4. Merge Sort
# 5. Dijkstra's Algorithm (It is an algorithm for finding the shortest paths between nodes in a weighted graph)

# Course: BIT2203 Data Structures & Algorithms



import heapq
# Heapq is used for Dijkstra's algorithm to implement a priority queue (Min Heap).


# ==================================================
# 1. LINEAR SEARCH
# ==================================================

def linear_search(arr, target):
    """
    Searches sequentially through a list.
    Time Complexity: O(n)
    Used when data is unsorted.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


# ==================================================
# 2. BINARY SEARCH
# ==================================================

def binary_search(arr, target):
    """
    Works only on sorted lists.
    Time Complexity: O(log n)
    Used in databases and search engines.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ==================================================
# 3. BUBBLE SORT
# ==================================================

def bubble_sort(arr):
    """
    Simple sorting algorithm.
    Time Complexity: O(n^2)
    Not efficient for large data.
    """

    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# ==================================================
# 4. MERGE SORT
# ==================================================

def merge_sort(arr):
    """
    Efficient divide-and-conquer sorting algorithm.
    Time Complexity: O(n log n)
    Used in large-scale systems.
    """

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ==================================================
# 5. DIJKSTRA'S ALGORITHM
# ==================================================

def dijkstra(graph, start):
    """
    Finds shortest path from start node to all other nodes.
    Uses priority queue (Min Heap).

    Time Complexity: O((V + E) log V)
    Used in:
    - Google Maps
    - Network routing
    """

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# ==================================================
# MAIN EXECUTION
# ==================================================

if __name__ == "__main__":

    print("\nALGORITHMS DEMONSTRATION")
    print("=" * 60)

    # ------------------------------------------
    # Search Algorithms
    # ------------------------------------------

    data = [5, 2, 9, 1, 7]
    sorted_data = sorted(data)

    print("Original List:", data)
    print("Sorted List:", sorted_data)

    print("\nLinear Search for 9:")
    print("Index:", linear_search(data, 9))

    print("\nBinary Search for 7:")
    print("Index:", binary_search(sorted_data, 7))

    # ------------------------------------------
    # Sorting Algorithms
    # ------------------------------------------

    print("\nBubble Sort:")
    print(bubble_sort(data.copy()))

    print("\nMerge Sort:")
    print(merge_sort(data.copy()))

    # ------------------------------------------
    # Dijkstra Algorithm
    # ------------------------------------------

    print("\nDijkstra's Algorithm:")

    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 5), ('D', 10)],
        'C': [('E', 3)],
        'D': [('F', 11)],
        'E': [('D', 4)],
        'F': []
    }

    shortest_paths = dijkstra(graph, 'A')

    print("Shortest paths from A:")
    for node, distance in shortest_paths.items():
        print(f"{node}: {distance}")

    print("=" * 60)
