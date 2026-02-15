# python_data_structures
This repository features the implementation of fundamental data structures and algorithmic analysis for Task 1.

Course: BIT 2203 Data Structures & Algorithms 

Task: Assignment 1 – Data Structures Classification 

Language Used: Python 

Group Members 

1. Aloo John – BSCCS/2025/40982 

2. Abraham Kibichii – BSCCS/2025/39564 

3. Natasha Mudavali -BSCCS/2025/41200 

4. Mohamed Amin - BSCCS/2025/41039 

5. John Timothy -  BSCCS/2025/35868 

6. Cliff Darren - BSCCS/2025/42307 

7. Gerald Wachira -  BSCCS/2025/40699 

8. Esther - BSCCS/2025/39862 

9. Franklin Njenga -BSCCS/2025/40683 

10. Lewis Thegetha -BSCCS/2025/69379 

 

1.Introduction 

Data Structures are methods of organizing and storing data in a computer so that it can be accessed and modified efficiently. Algorithms operate on these data structures to perform operations such as searching, sorting, inserting, and deleting. 

This project demonstrates: 

Classification of Data Structures 

Python implementation of each type 

Real-world applications 

Algorithms associated with them 

How data structures work within systems 

 

 2. Data Structure Classification 

According to standard classification, Data Structures are divided into: 

 

a. Primitive Data Structures 

Basic built-in data types that store single values. In Python, these include: 

Integer (int): Whole numbers. 

Float (float): Decimal values. 

Boolean (bool): Logical True/False. 

String (str): Character sequences. 

b. Non-Primitive Data Structures 

These are more complex and can store multiple values. They are further classified into: 

i. Linear Data Structures Data elements are arranged sequentially. 

List (Array), Stack, Queue, Tuple, Set, and Dictionary. 

ii. Non-Linear Data Structures Data elements are arranged hierarchically or interconnected. 

Tree and Graph. 

 

3. Python Implementations 

a. Primitive Data Structures 

Python 

# Primitive Data Structures implementation 
age = 21 
price = 199.99 
grade = 'A' 
is_student = True 
 
print(age, price, grade, is_student) 
 

Applications: 

Used in mathematical calculations, database fields, conditional logic, and system configuration values. 

 

b. Linear Data Structures 

i. List (Dynamic Array) 

Python 

students = ["John", "Mary", "Alex"] 
students.append("Brian") 
students.remove("Mary") 
print(students) 
 

Applications: Shopping carts, student management systems, task tracking. 

Time Complexity: Access:  O (1) | Insert/Delete:  O(n)  

ii. Stack (LIFO - Last In First Out) 

Python 

stack = [] 
stack.append("Page1") 
stack.append("Page2") 
stack.pop() 
print(stack) 
 

Applications: Browser history (Back button), Undo/Redo systems, Function call stacks. 

Algorithms: Depth First Search (DFS), Expression evaluation. 

Time Complexity: Push:  O (1) | Pop:  O (1) 

iii. Queue (FIFO - First In First Out) 

Python 

from collections import deque 
queue = deque() 
queue.append("Customer1") 
queue.append("Customer2") 
queue.popleft() 
print(queue) 
 

Applications: CPU scheduling, Printer queues, Call center systems. 

Algorithms: Breadth First Search (BFS). 

Time Complexity: Enqueue:  O (1) | Dequeue:  O (1) 

iv. Tuple (Immutable Structure) 

Python 

coordinates = (10, 20) 
print(coordinates) 
 

Applications: GPS systems, fixed database records. 

Why Used: Faster than lists and safe from accidental modification. 

v Set (Unique Elements) 

Python 

numbers = {1, 2, 3, 3, 4} 
print(numbers) # Output will only show {1, 2, 3, 4} 
 

Applications: Removing duplicates, membership testing, access control. 

Time Complexity: Search:  O (1) 

vi Dictionary (Hash Table) 

Python 

student = {"name": "John", "age": 21} 
print(student["name"]) 
 

Applications: JSON data, Databases, API responses, configuration storage. 

Time Complexity: Search:  O (1)   | Insert:  O (1) 

 

c. Non-Linear Data Structures 

i Tree (Binary Tree) 

Python 

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None 
 
root = Node(10) 
root.left = Node(5) 
root.right = Node(15) 
 

Applications: File systems, Database indexing (B-Trees), Search engines. 

Algorithms: Binary Search Tree (BST), Inorder/Preorder/Postorder traversals. 

ii Graph 

Python 

graph = { 
    "A": ["B", "C"], 
    "B": ["D"], 
    "C": [], 
    "D": [] 
} 
 

Applications: Google Maps navigation, Social networks, Network routing. 

Algorithms: Dijkstra’s Algorithm, BFS, DFS. 

 

4. Systems Applications 

Operating Systems: Process scheduling (Queue), Function calls (Stack), Memory management (Linked Lists). 

Databases: Indexing (B-Trees), Searching (Hash Tables), Record storage (Arrays). 

Web Applications: Session management (Dictionary), Undo features (Stack), Messaging (Queue). 

Search Engines: Page ranking (Graph algorithms), Autocomplete (Trie/Tree). 

 

5. Importance of Algorithms 

Algorithms define how operations are performed on data structures: 

Stack: Used by DFS for Graph traversal. 

Queue: Used by BFS for Level order traversal. 

Tree: Used by Binary Search for high-speed retrieval. 

Graph: Used by Dijkstra for finding the shortest path. 

 

 

6. Conclusion 

Choosing the correct data structure improves performance, memory efficiency, and scalability. Understanding these fundamentals allows developers to build optimized systems like databases and search engines. 

 

7. References 

Cormen, T. H., et al. (2009). Introduction to Algorithms. 

Goodrich, M. T., et al. (2014). Data Structures and Algorithms in Python. 

Python Official Documentation: https://docs.python.org/3/ 

Geeks for geeks https://www.geeksforgeeks.org/python/python-data-structures/ 

 

 
