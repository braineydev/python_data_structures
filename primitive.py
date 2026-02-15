
# primitive.py
# -----------------------------------------
# Demonstration of Primitive Data Structures in Python

# Primitive Data Structures:
# 1. int
# 2. float
# 3. bool
# 4. str (character & string)

# This file also demonstrates:
# - Basic operations
# - Simple algorithms using primitives
# - Practical system-like examples

# Course: BIT2203 Data Structures & Algorithms


# ==========================================
# 1. INTEGER (int)
# ==========================================

def integer_demo():
    """
    Demonstrates integer operations.
    Used in counting, indexing, IDs, and arithmetic.
    """

    age = 21
    year = 2026

    print("INTEGER DEMO")
    print("Age:", age)
    print("Year:", year)
    print("Sum:", age + year)
    print("Difference:", year - age)
    print("-" * 40)


# ==========================================
# 2. FLOAT (float)
# ==========================================

def float_demo():
    """
    Demonstrates float operations.
    Used in financial systems, scientific calculations, and measurements.
    """

    price = 199.99
    tax_rate = 0.16

    total_price = price + (price * tax_rate)

    print("FLOAT DEMO")
    print("Original Price:", price)
    print("Tax Rate:", tax_rate)
    print("Total Price with Tax:", round(total_price, 2))
    print("-" * 40)


# ==========================================
# 3. BOOLEAN (bool)
# ==========================================

def boolean_demo():
    """
    Demonstrates boolean values.
    Used in decision making, authentication, and control flow.
    """

    is_logged_in = True
    has_permission = False

    print("BOOLEAN DEMO")
    print("Is Logged In:", is_logged_in)
    print("Has Permission:", has_permission)

    # Logical operation
    access_granted = is_logged_in and has_permission
    print("Access Granted:", access_granted)
    print("-" * 40)


# ==========================================
# 4. STRING (str)
# ==========================================

def string_demo():
    """
    Demonstrates string operations.
    Used in user input, databases, text processing.
    """

    first_name = "John"
    last_name = "Brainy"

    full_name = first_name + " " + last_name

    print("STRING DEMO")
    print("Full Name:", full_name)
    print("Name Length:", len(full_name))
    print("Uppercase:", full_name.upper())
    print("-" * 40)


# ==========================================
# 5. SIMPLE ALGORITHM USING PRIMITIVES
# ==========================================

def even_or_odd(number):
    """
    Simple algorithm using primitive int and bool.
    Determines if a number is even or odd.
    """

    if number % 2 == 0:
        return True
    else:
        return False


# ==========================================
# 6. MAIN EXECUTION
# ==========================================

if __name__ == "__main__":

    print("\nPRIMITIVE DATA STRUCTURES DEMONSTRATION")
    print("=" * 40)

    integer_demo()
    float_demo()
    boolean_demo()
    string_demo()

    # Testing simple algorithm
    test_number = 10
    result = even_or_odd(test_number)

    print("ALGORITHM DEMO")
    print(f"Is {test_number} even?", result)
    print("=" * 40)
