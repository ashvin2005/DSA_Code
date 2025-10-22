"""
Singly Linked List Implementation
================================

Data Structure Description:
A Linked List is a linear data structure where elements (nodes) are not stored in
contiguous memory locations. Each node contains data and a reference (link) to the
next node in the sequence. This allows for efficient insertion and deletion operations.

Types of operations:
- Insertion: At beginning O(1), at end O(n), at position O(n)
- Deletion: At beginning O(1), at end O(n), at position O(n)
- Search: O(n)
- Access: O(n)

Space Complexity: O(n) where n is the number of nodes

Advantages:
- Dynamic size (grows/shrinks as needed)
- Efficient insertion/deletion (no shifting required)
- No memory wastage

Disadvantages:
- No random access (must traverse from head)
- Extra memory for storing references
- Not cache-friendly

Applications:
- Implementation of stacks and queues
- Dynamic memory allocation
- Symbol table management in compilers
- Undo functionality in applications
- Browser history navigation
"""


class Node:
    """
    Node class representing a single element in the linked list.
    """
    
    def __init__(self, data):
        """
        Initialize a node with data.
        
        Args:
            data: The value to store in the node
        """
        self.data = data
        self.next = None
    
    def __str__(self):
        """String representation of the node."""
        return str(self.data)


class LinkedList:
    """
    Singly Linked List implementation with comprehensive operations.
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """
        Check if the linked list is empty.
        
        Returns:
            bool: True if empty, False otherwise
        """
        return self.head is None
    
    def __len__(self):
        """Return the number of nodes in the linked list."""
        return self.size
    
    def append(self, data):
        """
        Add a new node at the end of the linked list.
        
        Args:
            data: Value to add
        
        Time Complexity: O(n)
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def prepend(self, data):
        """
        Add a new node at the beginning of the linked list.
        
        Args:
            data: Value to add
        
        Time Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_position(self, data, position):
        """
        Insert a new node at a specific position.
        
        Args:
            data: Value to insert
            position (int): Position to insert at (0-indexed)
        
        Raises:
            IndexError: If position is invalid
        
        Time Complexity: O(n)
        """
        if position < 0 or position > self.size:
            raise IndexError(f"Position {position} is out of range")
        
        if position == 0:
            self.prepend(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_first(self):
        """
        Delete the first node from the linked list.
        
        Returns:
            The data from the deleted node
        
        Raises:
            IndexError: If list is empty
        
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot delete from empty list")
        
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def delete_last(self):
        """
        Delete the last node from the linked list.
        
        Returns:
            The data from the deleted node
        
        Raises:
            IndexError: If list is empty
        
        Time Complexity: O(n)
        """
        if self.is_empty():
            raise IndexError("Cannot delete from empty list")
        
        if self.head.next is None:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        
        current = self.head
        while current.next.next:
            current = current.next
        
        data = current.next.data
        current.next = None
        self.size -= 1
        return data
    
    def delete_at_position(self, position):
        """
        Delete a node at a specific position.
        
        Args:
            position (int): Position to delete from (0-indexed)
        
        Returns:
            The data from the deleted node
        
        Raises:
            IndexError: If position is invalid
        
        Time Complexity: O(n)
        """
        if position < 0 or position >= self.size:
            raise IndexError(f"Position {position} is out of range")
        
        if position == 0:
            return self.delete_first()
        
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return data
    
    def delete_by_value(self, value):
        """
        Delete the first node with the specified value.
        
        Args:
            value: Value to delete
        
        Returns:
            bool: True if deleted, False if not found
        
        Time Complexity: O(n)
        """
        if self.is_empty():
            return False
        
        # Check if head needs to be deleted
        if self.head.data == value:
            self.delete_first()
            return True
        
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def search(self, value):
        """
        Search for a value in the linked list.
        
        Args:
            value: Value to search for
        
        Returns:
            int: Index of the value if found, -1 otherwise
        
        Time Complexity: O(n)
        """
        current = self.head
        index = 0
        
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def get(self, position):
        """
        Get the value at a specific position.
        
        Args:
            position (int): Position to get (0-indexed)
        
        Returns:
            The data at the specified position
        
        Raises:
            IndexError: If position is invalid
        
        Time Complexity: O(n)
        """
        if position < 0 or position >= self.size:
            raise IndexError(f"Position {position} is out of range")
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        return current.data
    
    def reverse(self):
        """
        Reverse the linked list in place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def find_middle(self):
        """
        Find the middle element of the linked list using slow-fast pointer technique.
        
        Returns:
            The data of the middle node, None if empty
        
        Time Complexity: O(n)
        """
        if self.is_empty():
            return None
        
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def has_cycle(self):
        """
        Detect if the linked list has a cycle using Floyd's algorithm.
        
        Returns:
            bool: True if cycle exists, False otherwise
        
        Time Complexity: O(n)
        """
        if self.is_empty():
            return False
        
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
    
    def remove_duplicates(self):
        """
        Remove duplicate values from the linked list (keeps first occurrence).
        
        Time Complexity: O(n²) with nested loops, O(n) with hash set
        """
        if self.is_empty():
            return
        
        seen = set()
        current = self.head
        seen.add(current.data)
        
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
                self.size -= 1
            else:
                seen.add(current.next.data)
                current = current.next
    
    def to_list(self):
        """
        Convert linked list to Python list.
        
        Returns:
            list: List of all values in the linked list
        """
        result = []
        current = self.head
        
        while current:
            result.append(current.data)
            current = current.next
        
        return result
    
    def clear(self):
        """Clear the linked list."""
        self.head = None
        self.size = 0
    
    def __str__(self):
        """String representation of the linked list."""
        if self.is_empty():
            return "Empty List"
        
        values = self.to_list()
        return " -> ".join(map(str, values)) + " -> None"
    
    def __repr__(self):
        """Official string representation."""
        return f"LinkedList({self.to_list()})"
    
    def __iter__(self):
        """Make the linked list iterable."""
        current = self.head
        while current:
            yield current.data
            current = current.next


def test_linked_list():
    """Comprehensive test cases for linked list implementation."""
    print("Testing Linked List Implementation")
    print("=" * 50)
    
    # Test 1: Creation and basic operations
    print("\nTest 1: Creation and Basic Operations")
    ll = LinkedList()
    assert ll.is_empty() == True, "New list should be empty"
    assert len(ll) == 0, "Size should be 0"
    
    # Test append
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(f"After appending 1, 2, 3: {ll}")
    assert len(ll) == 3, "Size should be 3"
    assert ll.to_list() == [1, 2, 3], "List values incorrect"
    
    # Test 2: Prepend
    print("\nTest 2: Prepend Operation")
    ll.prepend(0)
    print(f"After prepending 0: {ll}")
    assert ll.to_list() == [0, 1, 2, 3], "Prepend failed"
    
    # Test 3: Insert at position
    print("\nTest 3: Insert at Position")
    ll.insert_at_position(1.5, 2)
    print(f"After inserting 1.5 at position 2: {ll}")
    assert ll.to_list() == [0, 1, 1.5, 2, 3], "Insert at position failed"
    
    # Test 4: Search
    print("\nTest 4: Search Operation")
    assert ll.search(1.5) == 2, "Search failed"
    assert ll.search(99) == -1, "Search for non-existent value failed"
    print("Search operations passed ✅")
    
    # Test 5: Get
    print("\nTest 5: Get Operation")
    assert ll.get(0) == 0, "Get at position 0 failed"
    assert ll.get(2) == 1.5, "Get at position 2 failed"
    print("Get operations passed ✅")
    
    # Test 6: Delete operations
    print("\nTest 6: Delete Operations")
    ll.delete_first()
    print(f"After deleting first: {ll}")
    assert ll.to_list() == [1, 1.5, 2, 3], "Delete first failed"
    
    ll.delete_last()
    print(f"After deleting last: {ll}")
    assert ll.to_list() == [1, 1.5, 2], "Delete last failed"
    
    ll.delete_at_position(1)
    print(f"After deleting at position 1: {ll}")
    assert ll.to_list() == [1, 2], "Delete at position failed"
    
    # Test 7: Reverse
    print("\nTest 7: Reverse Operation")
    ll2 = LinkedList()
    for i in range(1, 6):
        ll2.append(i)
    print(f"Original: {ll2}")
    ll2.reverse()
    print(f"Reversed: {ll2}")
    assert ll2.to_list() == [5, 4, 3, 2, 1], "Reverse failed"
    
    # Test 8: Find middle
    print("\nTest 8: Find Middle Element")
    ll3 = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        ll3.append(i)
    middle = ll3.find_middle()
    print(f"List: {ll3}")
    print(f"Middle element: {middle}")
    assert middle == 3, "Find middle failed for odd length"
    
    # Test 9: Remove duplicates
    print("\nTest 9: Remove Duplicates")
    ll4 = LinkedList()
    for val in [1, 2, 2, 3, 3, 3, 4, 5, 5]:
        ll4.append(val)
    print(f"Before: {ll4}")
    ll4.remove_duplicates()
    print(f"After:  {ll4}")
    assert ll4.to_list() == [1, 2, 3, 4, 5], "Remove duplicates failed"
    
    # Test 10: Iteration
    print("\nTest 10: Iteration")
    ll5 = LinkedList()
    for i in range(1, 4):
        ll5.append(i)
    result = [x for x in ll5]
    print(f"Iteration result: {result}")
    assert result == [1, 2, 3], "Iteration failed"
    
    print("\n" + "=" * 50)
    print("All tests passed! 🎉")


def interactive_demo():
    """Interactive demonstration of linked list."""
    print("\nInteractive Linked List Demo")
    print("=" * 40)
    
    ll = LinkedList()
    
    while True:
        print(f"\nCurrent List: {ll}")
        print(f"Size: {len(ll)}")
        print("\nChoose an operation:")
        print("1. Append")
        print("2. Prepend")
        print("3. Insert at position")
        print("4. Delete first")
        print("5. Delete last")
        print("6. Delete by value")
        print("7. Search")
        print("8. Reverse")
        print("9. Find middle")
        print("10. Remove duplicates")
        print("11. Exit")
        
        try:
            choice = input("Enter choice (1-11): ").strip()
            
            if choice == '1':
                value = input("Enter value to append: ")
                ll.append(value)
                print(f"✅ Appended {value}")
            
            elif choice == '2':
                value = input("Enter value to prepend: ")
                ll.prepend(value)
                print(f"✅ Prepended {value}")
            
            elif choice == '3':
                value = input("Enter value: ")
                position = int(input("Enter position: "))
                ll.insert_at_position(value, position)
                print(f"✅ Inserted {value} at position {position}")
            
            elif choice == '4':
                if not ll.is_empty():
                    deleted = ll.delete_first()
                    print(f"✅ Deleted first element: {deleted}")
                else:
                    print("❌ List is empty")
            
            elif choice == '5':
                if not ll.is_empty():
                    deleted = ll.delete_last()
                    print(f"✅ Deleted last element: {deleted}")
                else:
                    print("❌ List is empty")
            
            elif choice == '6':
                value = input("Enter value to delete: ")
                if ll.delete_by_value(value):
                    print(f"✅ Deleted {value}")
                else:
                    print(f"❌ {value} not found")
            
            elif choice == '7':
                value = input("Enter value to search: ")
                index = ll.search(value)
                if index != -1:
                    print(f"✅ Found at index {index}")
                else:
                    print(f"❌ {value} not found")
            
            elif choice == '8':
                ll.reverse()
                print("✅ List reversed")
            
            elif choice == '9':
                middle = ll.find_middle()
                if middle is not None:
                    print(f"✅ Middle element: {middle}")
                else:
                    print("❌ List is empty")
            
            elif choice == '10':
                ll.remove_duplicates()
                print("✅ Duplicates removed")
            
            elif choice == '11':
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter 1-11.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except IndexError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Run comprehensive tests
    test_linked_list()
    
    # Demonstrate usage
    print("\n" + "=" * 60)
    print("DEMONSTRATION: Linked List in Action")
    print("=" * 60)
    
    demo_list = LinkedList()
    print("Creating a linked list with values 10, 20, 30, 40, 50")
    for val in [10, 20, 30, 40, 50]:
        demo_list.append(val)
    
    print(f"List: {demo_list}")
    print(f"Length: {len(demo_list)}")
    print(f"Middle element: {demo_list.find_middle()}")
    
    print("\nReversing the list...")
    demo_list.reverse()
    print(f"Reversed: {demo_list}")
    
    # Optional: Run interactive demo
    # Uncomment the line below to try the interactive version
    # interactive_demo()