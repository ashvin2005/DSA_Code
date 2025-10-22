"""
Stack Data Structure Implementation
==================================

Data Structure Description:
A Stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
The last element added to the stack is the first one to be removed. Think of it like
a stack of plates - you can only add or remove plates from the top.

Core Operations:
- push(item): Add an item to the top of the stack - O(1)
- pop(): Remove and return the top item - O(1)
- peek(): Return the top item without removing it - O(1)
- is_empty(): Check if stack is empty - O(1)
- size(): Return the number of items - O(1)

Space Complexity: O(n) where n is the number of elements

Applications:
- Function call stack in programming languages
- Undo/Redo functionality in applications
- Expression evaluation and syntax parsing
- Backtracking algorithms (maze solving, DFS)
- Browser history (back button)
- Balanced parentheses checking
"""


class Stack:
    """
    Stack implementation using Python list (dynamic array).
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to add
        
        Time Complexity: O(1) amortized
        """
        self.items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item
        
        Raises:
            IndexError: If the stack is empty
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """
        Return the top item without removing it.
        
        Returns:
            The top item
        
        Raises:
            IndexError: If the stack is empty
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek at empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if empty, False otherwise
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Return the number of items in the stack.
        
        Returns:
            int: Number of items
        """
        return len(self.items)
    
    def clear(self):
        """Clear all items from the stack."""
        self.items = []
    
    def __len__(self):
        """Return the size of the stack."""
        return len(self.items)
    
    def __bool__(self):
        """Return True if stack is not empty."""
        return not self.is_empty()
    
    def __str__(self):
        """String representation of the stack."""
        if self.is_empty():
            return "Stack([])"
        return f"Stack({self.items}) <- Top"
    
    def __repr__(self):
        """Official string representation."""
        return f"Stack({self.items})"


class StackNode:
    """Node class for linked list based stack."""
    
    def __init__(self, data):
        """Initialize a node."""
        self.data = data
        self.next = None


class LinkedStack:
    """
    Stack implementation using linked list.
    More memory efficient for dynamic operations.
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self.top = None
        self._size = 0
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to add
        
        Time Complexity: O(1)
        """
        new_node = StackNode(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item
        
        Raises:
            IndexError: If the stack is empty
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return data
    
    def peek(self):
        """
        Return the top item without removing it.
        
        Returns:
            The top item
        
        Raises:
            IndexError: If the stack is empty
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek at empty stack")
        return self.top.data
    
    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None
    
    def size(self):
        """Return the number of items in the stack."""
        return self._size
    
    def __len__(self):
        """Return the size of the stack."""
        return self._size
    
    def __str__(self):
        """String representation of the stack."""
        if self.is_empty():
            return "LinkedStack([])"
        
        items = []
        current = self.top
        while current:
            items.append(current.data)
            current = current.next
        return f"LinkedStack({items}) <- Top"


def is_balanced_parentheses(expression):
    """
    Check if parentheses in an expression are balanced using stack.
    
    Args:
        expression (str): String containing parentheses
    
    Returns:
        bool: True if balanced, False otherwise
    
    Example:
        >>> is_balanced_parentheses("(()())")
        True
        >>> is_balanced_parentheses("(()")
        False
    """
    stack = Stack()
    opening = "({["
    closing = ")}]"
    pairs = {"(": ")", "{": "}", "[": "]"}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()


def evaluate_postfix(expression):
    """
    Evaluate a postfix (Reverse Polish Notation) expression.
    
    Args:
        expression (str): Space-separated postfix expression
    
    Returns:
        float: Result of the evaluation
    
    Example:
        >>> evaluate_postfix("3 4 + 2 * 7 /")
        2.0
    """
    stack = Stack()
    tokens = expression.split()
    
    for token in tokens:
        if token in "+-*/":
            if stack.size() < 2:
                raise ValueError("Invalid expression")
            
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                result = a / b
            
            stack.push(result)
        else:
            try:
                stack.push(float(token))
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
    
    if stack.size() != 1:
        raise ValueError("Invalid expression")
    
    return stack.pop()


def infix_to_postfix(expression):
    """
    Convert infix expression to postfix notation.
    
    Args:
        expression (str): Infix expression (e.g., "A + B * C")
    
    Returns:
        str: Postfix expression
    
    Example:
        >>> infix_to_postfix("A + B * C")
        'A B C * +'
    """
    stack = Stack()
    output = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    tokens = expression.split()
    
    for token in tokens:
        if token.isalnum():  # Operand
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            if not stack.is_empty():
                stack.pop()  # Remove '('
        elif token in precedence:  # Operator
            while (not stack.is_empty() and 
                   stack.peek() != '(' and
                   stack.peek() in precedence and
                   precedence[stack.peek()] >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)
    
    while not stack.is_empty():
        output.append(stack.pop())
    
    return ' '.join(output)


def reverse_string(s):
    """
    Reverse a string using a stack.
    
    Args:
        s (str): Input string
    
    Returns:
        str: Reversed string
    """
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str


def next_greater_element(arr):
    """
    Find the next greater element for each element in an array.
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Array where each element is the next greater element
              or -1 if no greater element exists
    
    Example:
        >>> next_greater_element([4, 5, 2, 10])
        [5, 10, 10, -1]
    """
    n = len(arr)
    result = [-1] * n
    stack = Stack()
    
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Remove elements smaller than current
        while not stack.is_empty() and stack.peek() <= arr[i]:
            stack.pop()
        
        # If stack not empty, top is next greater
        if not stack.is_empty():
            result[i] = stack.peek()
        
        # Push current element
        stack.push(arr[i])
    
    return result


def test_stack():
    """Comprehensive test cases for stack implementations."""
    print("Testing Stack Implementations")
    print("=" * 50)
    
    # Test 1: Array-based stack - Basic operations
    print("\nTest 1: Array-based Stack - Basic Operations")
    stack = Stack()
    assert stack.is_empty() == True, "New stack should be empty"
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"After pushing 1, 2, 3: {stack}")
    assert stack.size() == 3, "Size should be 3"
    assert stack.peek() == 3, "Top should be 3"
    
    popped = stack.pop()
    print(f"Popped: {popped}")
    assert popped == 3, "Should pop 3"
    assert stack.size() == 2, "Size should be 2"
    print("Array-based stack tests passed ✅")
    
    # Test 2: Linked list-based stack
    print("\nTest 2: Linked List-based Stack")
    lstack = LinkedStack()
    lstack.push(10)
    lstack.push(20)
    lstack.push(30)
    print(f"After pushing 10, 20, 30: {lstack}")
    assert lstack.peek() == 30, "Top should be 30"
    assert lstack.pop() == 30, "Should pop 30"
    assert lstack.size() == 2, "Size should be 2"
    print("Linked stack tests passed ✅")
    
    # Test 3: Balanced parentheses
    print("\nTest 3: Balanced Parentheses")
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(())", True),
        ("([{}])", True),
        ("(()", False),
        ("(]", False),
        ("([)]", False),
    ]
    
    for expr, expected in test_cases:
        result = is_balanced_parentheses(expr)
        print(f"'{expr}' -> {result}")
        assert result == expected, f"Failed for {expr}"
    print("Balanced parentheses tests passed ✅")
    
    # Test 4: Postfix evaluation
    print("\nTest 4: Postfix Expression Evaluation")
    assert evaluate_postfix("3 4 +") == 7, "3 + 4 should be 7"
    assert evaluate_postfix("5 1 2 + 4 * + 3 -") == 14, "Complex expression failed"
    print("Postfix evaluation tests passed ✅")
    
    # Test 5: Infix to postfix
    print("\nTest 5: Infix to Postfix Conversion")
    result = infix_to_postfix("A + B")
    print(f"'A + B' -> '{result}'")
    assert result == "A B +", "Simple conversion failed"
    
    result = infix_to_postfix("A + B * C")
    print(f"'A + B * C' -> '{result}'")
    assert result == "A B C * +", "Precedence handling failed"
    print("Infix to postfix tests passed ✅")
    
    # Test 6: String reversal
    print("\nTest 6: String Reversal")
    assert reverse_string("hello") == "olleh", "Reversal failed"
    assert reverse_string("12345") == "54321", "Reversal failed"
    print("String reversal tests passed ✅")
    
    # Test 7: Next greater element
    print("\nTest 7: Next Greater Element")
    result = next_greater_element([4, 5, 2, 10])
    print(f"Input: [4, 5, 2, 10]")
    print(f"Next Greater: {result}")
    assert result == [5, 10, 10, -1], "Next greater element failed"
    print("Next greater element tests passed ✅")
    
    # Test 8: Edge cases
    print("\nTest 8: Edge Cases")
    empty_stack = Stack()
    try:
        empty_stack.pop()
        assert False, "Should raise exception"
    except IndexError:
        print("Empty stack pop raises exception ✅")
    
    try:
        empty_stack.peek()
        assert False, "Should raise exception"
    except IndexError:
        print("Empty stack peek raises exception ✅")
    
    print("\n" + "=" * 50)
    print("All tests passed! 🎉")


if __name__ == "__main__":
    # Run comprehensive tests
    test_stack()
    
    # Demonstrate usage
    print("\n" + "=" * 60)
    print("DEMONSTRATION: Stack Applications")
    print("=" * 60)
    
    # Demo 1: Basic stack operations
    print("\n1. Basic Stack Operations:")
    demo_stack = Stack()
    for val in [10, 20, 30, 40, 50]:
        demo_stack.push(val)
        print(f"Pushed {val}: {demo_stack}")
    
    print("\nPopping elements:")
    while not demo_stack.is_empty():
        print(f"Popped {demo_stack.pop()}: {demo_stack}")
    
    # Demo 2: Balanced parentheses
    print("\n2. Balanced Parentheses Check:")
    expressions = ["((()))", "((())", "{[()]}"]
    for expr in expressions:
        result = is_balanced_parentheses(expr)
        print(f"{expr} -> {'Balanced' if result else 'Not Balanced'}")
    
    # Demo 3: Expression evaluation
    print("\n3. Postfix Expression Evaluation:")
    postfix = "5 3 + 2 *"
    result = evaluate_postfix(postfix)
    print(f"'{postfix}' = {result}")