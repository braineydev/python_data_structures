
# linear_structures.py
# ------------------------------------------------
# Demonstration of Linear Data Structures in Python

# Linear Data Structures:
# 1. List (Dynamic Array)
# 2. Stack (LIFO)
# 3. Queue (FIFO)
# 4. Tuple (Immutable sequence)
# 5. Set (Unique unordered collection)
# 6. Dictionary (Key-Value mapping / Hash Table)

# Includes:
# - Practical examples
# - Simple implementation examples
# - Time complexity notes

# Course: BIT2203 Data Structures & Algorithms


from collections import deque


# ==================================================
# 1. LIST (Dynamic Array)
# ==================================================

def list_demo():
    """
    Lists store elements sequentially.
    Used in shopping carts, student lists, logs.

    Time Complexity:
    - Access: O(1)
    - Insert/Delete (middle): O(n)
    """

    students = ["John", "Mary", "Alex"]

    students.append("Brian")   # O(1)
    students.remove("Mary")    # O(n)

    print("LIST DEMO")
    print("Students:", students)
    print("First Student:", students[0])
    print("-" * 50)


# ==================================================
# 2. STACK (LIFO - Last In First Out)
# ==================================================

def stack_demo():
    """
    Stack follows LIFO principle.
    Used in:
    - Browser history
    - Undo/Redo
    - Function call stack

    Operations:
    - push (append)
    - pop
    Time Complexity: O(1)
    """

    stack = []

    stack.append("Page1")
    stack.append("Page2")
    stack.append("Page3")

    last_page = stack.pop()

    print("STACK DEMO")
    print("Current Stack:", stack)
    print("Popped Element:", last_page)
    print("-" * 50)


# ==================================================
# 3. QUEUE (FIFO - First In First Out)
# ==================================================

def queue_demo():
    """
    Queue follows FIFO principle.
    Used in:
    - CPU scheduling
    - Printer queues
    - Call centers

    Time Complexity:
    - Enqueue: O(1)
    - Dequeue: O(1)
    """

    queue = deque()

    queue.append("Customer1")
    queue.append("Customer2")
    queue.append("Customer3")

    served_customer = queue.popleft()

    print("QUEUE DEMO")
    print("Remaining Queue:", list(queue))
    print("Served Customer:", served_customer)
    print("-" * 50)


# ==================================================
# 4. TUPLE (Immutable Structure)
# ==================================================

def tuple_demo():
    """
    Tuple is immutable (cannot be modified).
    Used in:
    - Coordinates
    - Fixed records
    - Database rows

    Faster than list for read-only data.
    """

    coordinates = (10, 20)

    print("TUPLE DEMO")
    print("Coordinates:", coordinates)
    print("X value:", coordinates[0])
    print("-" * 50)


# ==================================================
# 5. SET (No duplicates)
# ==================================================

def set_demo():
    """
    Set stores unique values only.
    Used in:
    - Removing duplicates
    - Membership testing

    Average Time Complexity:
    - Add/Search/Delete: O(1)
    """

    numbers = {1, 2, 3, 3, 4}
    numbers.add(5)

    print("SET DEMO")
    print("Unique Numbers:", numbers)
    print("Is 3 in set?", 3 in numbers)
    print("-" * 50)


# ==================================================
# 6. DICTIONARY (Hash Table)
# ==================================================

def dictionary_demo():
    """
    Dictionary stores key-value pairs.
    Implemented using hash tables.

    Used in:
    - JSON data
    - APIs
    - Databases
    - Configuration storage

    Average Time Complexity:
    - Access: O(1)
    - Insert: O(1)
    """

    student = {
        "name": "John",
        "age": 21,
        "course": "Computer Science"
    }

    student["year"] = 2  # Insert

    print("DICTIONARY DEMO")
    print("Student Info:", student)
    print("Student Name:", student["name"])
    print("-" * 50)


# ==================================================
# 7. SIMPLE SEARCH ALGORITHM (LINEAR SEARCH)
# ==================================================

def linear_search(data, target):
    """
    Linear Search Algorithm
    Works well with Lists.

    Time Complexity: O(n)
    """

    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


# ==================================================
# 8. MAIN EXECUTION
# ==================================================

if __name__ == "__main__":

    print("\nLINEAR DATA STRUCTURES DEMONSTRATION")
    print("=" * 50)

    list_demo()
    stack_demo()
    queue_demo()
    tuple_demo()
    set_demo()
    dictionary_demo()

    # Testing Linear Search
    sample_list = [10, 20, 30, 40, 50]
    target_value = 30

    position = linear_search(sample_list, target_value)

    print("LINEAR SEARCH DEMO")
    print("List:", sample_list)
    print("Target:", target_value)
    print("Position Found:", position)
    print("=" * 50)
