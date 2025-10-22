"""
Binary Search Tree (BST) Implementation
======================================

Data Structure Description:
A Binary Search Tree is a binary tree data structure where each node has at most two children,
and for every node:
- All values in the left subtree are less than the node's value
- All values in the right subtree are greater than the node's value
- Both left and right subtrees are also binary search trees

This property allows for efficient searching, insertion, and deletion operations.

Time Complexities:
- Search: O(log n) average, O(n) worst case
- Insertion: O(log n) average, O(n) worst case  
- Deletion: O(log n) average, O(n) worst case
- Traversal: O(n)

Space Complexity: O(n) for storing n nodes, O(log n) for recursion stack

Applications:
- Database indexing
- Expression parsing
- File system organization
- Priority queues
- Autocomplete features
"""


class TreeNode:
    """
    Node class for Binary Search Tree.
    """
    
    def __init__(self, value):
        """
        Initialize a tree node.
        
        Args:
            value: The value to store in the node
        """
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        """String representation of the node."""
        return str(self.value)


class BinarySearchTree:
    """
    Binary Search Tree implementation with comprehensive operations.
    """
    
    def __init__(self):
        """Initialize an empty BST."""
        self.root = None
        self.size = 0
    
    def insert(self, value):
        """
        Insert a value into the BST.
        
        Args:
            value: Value to insert
        
        Returns:
            bool: True if inserted, False if value already exists
        """
        if self.root is None:
            self.root = TreeNode(value)
            self.size += 1
            return True
        
        return self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """
        Recursive helper method for insertion.
        
        Args:
            node (TreeNode): Current node
            value: Value to insert
        
        Returns:
            bool: True if inserted, False if duplicate
        """
        if value == node.value:
            return False  # Duplicate values not allowed
        
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
                self.size += 1
                return True
            else:
                return self._insert_recursive(node.left, value)
        else:  # value > node.value
            if node.right is None:
                node.right = TreeNode(value)
                self.size += 1
                return True
            else:
                return self._insert_recursive(node.right, value)
    
    def search(self, value):
        """
        Search for a value in the BST.
        
        Args:
            value: Value to search for
        
        Returns:
            bool: True if found, False otherwise
        """
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """
        Recursive helper method for searching.
        
        Args:
            node (TreeNode): Current node
            value: Value to search for
        
        Returns:
            bool: True if found, False otherwise
        """
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def delete(self, value):
        """
        Delete a value from the BST.
        
        Args:
            value: Value to delete
        
        Returns:
            bool: True if deleted, False if not found
        """
        initial_size = self.size
        self.root = self._delete_recursive(self.root, value)
        return self.size < initial_size
    
    def _delete_recursive(self, node, value):
        """
        Recursive helper method for deletion.
        
        Args:
            node (TreeNode): Current node
            value: Value to delete
        
        Returns:
            TreeNode: New root of this subtree
        """
        if node is None:
            return node
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node to be deleted found
            self.size -= 1
            
            # Case 1: Node with only right child or no child
            if node.left is None:
                return node.right
            
            # Case 2: Node with only left child
            if node.right is None:
                return node.left
            
            # Case 3: Node with two children
            # Get the inorder successor (smallest in right subtree)
            successor = self._find_min_node(node.right)
            
            # Copy the successor's value to this node
            node.value = successor.value
            
            # Delete the successor
            node.right = self._delete_recursive(node.right, successor.value)
            self.size += 1  # Compensate for the extra decrement above
        
        return node
    
    def _find_min_node(self, node):
        """
        Find the node with minimum value in a subtree.
        
        Args:
            node (TreeNode): Root of subtree
        
        Returns:
            TreeNode: Node with minimum value
        """
        while node.left is not None:
            node = node.left
        return node
    
    def find_min(self):
        """
        Find the minimum value in the BST.
        
        Returns:
            Value of minimum node, None if tree is empty
        """
        if self.root is None:
            return None
        
        node = self._find_min_node(self.root)
        return node.value
    
    def find_max(self):
        """
        Find the maximum value in the BST.
        
        Returns:
            Value of maximum node, None if tree is empty
        """
        if self.root is None:
            return None
        
        node = self.root
        while node.right is not None:
            node = node.right
        return node.value
    
    def inorder_traversal(self):
        """
        Perform inorder traversal (Left -> Root -> Right).
        This gives values in sorted order for BST.
        
        Returns:
            list: Values in inorder sequence
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Recursive helper for inorder traversal."""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """
        Perform preorder traversal (Root -> Left -> Right).
        
        Returns:
            list: Values in preorder sequence
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Recursive helper for preorder traversal."""
        if node is not None:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """
        Perform postorder traversal (Left -> Right -> Root).
        
        Returns:
            list: Values in postorder sequence
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """Recursive helper for postorder traversal."""
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
    
    def level_order_traversal(self):
        """
        Perform level-order traversal (breadth-first).
        
        Returns:
            list: Values in level-order sequence
        """
        if self.root is None:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        
        return result
    
    def height(self):
        """
        Calculate the height of the BST.
        
        Returns:
            int: Height of the tree (-1 for empty tree)
        """
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """Recursive helper for height calculation."""
        if node is None:
            return -1
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        
        return 1 + max(left_height, right_height)
    
    def is_valid_bst(self):
        """
        Check if the tree is a valid BST.
        
        Returns:
            bool: True if valid BST, False otherwise
        """
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))
    
    def _is_valid_bst_recursive(self, node, min_val, max_val):
        """Recursive helper for BST validation."""
        if node is None:
            return True
        
        if node.value <= min_val or node.value >= max_val:
            return False
        
        return (self._is_valid_bst_recursive(node.left, min_val, node.value) and
                self._is_valid_bst_recursive(node.right, node.value, max_val))
    
    def __len__(self):
        """Return the number of nodes in the BST."""
        return self.size
    
    def __bool__(self):
        """Return True if BST is not empty."""
        return self.root is not None
    
    def __contains__(self, value):
        """Check if value exists in BST using 'in' operator."""
        return self.search(value)
    
    def display_tree(self):
        """
        Display the tree structure in a readable format.
        """
        if self.root is None:
            print("Empty tree")
            return
        
        print("Tree structure:")
        self._display_recursive(self.root, "", True)
    
    def _display_recursive(self, node, prefix, is_last):
        """Recursive helper for tree display."""
        if node is not None:
            print(prefix + ("└── " if is_last else "├── ") + str(node.value))
            
            children = []
            if node.left is not None:
                children.append(('left', node.left))
            if node.right is not None:
                children.append(('right', node.right))
            
            for i, (side, child) in enumerate(children):
                is_last_child = (i == len(children) - 1)
                new_prefix = prefix + ("    " if is_last else "│   ")
                self._display_recursive(child, new_prefix, is_last_child)


def test_binary_search_tree():
    """Comprehensive test cases for Binary Search Tree."""
    print("Testing Binary Search Tree")
    print("=" * 50)
    
    # Test 1: Basic operations
    print("\nTest 1: Basic Operations")
    bst = BinarySearchTree()
    
    # Test insertion
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        assert bst.insert(val) == True, f"Failed to insert {val}"
    
    print(f"Inserted values: {values}")
    print(f"Tree size: {len(bst)}")
    print(f"Inorder traversal: {bst.inorder_traversal()}")
    
    # Test search
    assert bst.search(40) == True, "Search failed for existing value"
    assert bst.search(100) == False, "Search failed for non-existing value"
    
    # Test min/max
    assert bst.find_min() == 20, "Find min failed"
    assert bst.find_max() == 80, "Find max failed"
    
    # Test 2: Traversals
    print("\nTest 2: Tree Traversals")
    print(f"Inorder:    {bst.inorder_traversal()}")
    print(f"Preorder:   {bst.preorder_traversal()}")
    print(f"Postorder:  {bst.postorder_traversal()}")
    print(f"Level-order: {bst.level_order_traversal()}")
    
    # Test 3: Deletion
    print("\nTest 3: Deletion")
    print("Before deletion:")
    bst.display_tree()
    
    # Delete leaf node
    assert bst.delete(20) == True, "Failed to delete leaf node"
    print(f"After deleting 20: {bst.inorder_traversal()}")
    
    # Delete node with one child
    assert bst.delete(30) == True, "Failed to delete node with one child"
    print(f"After deleting 30: {bst.inorder_traversal()}")
    
    # Delete node with two children
    assert bst.delete(50) == True, "Failed to delete node with two children"
    print(f"After deleting 50: {bst.inorder_traversal()}")
    
    print("After deletions:")
    bst.display_tree()
    
    # Test 4: Edge cases
    print("\nTest 4: Edge Cases")
    empty_bst = BinarySearchTree()
    assert len(empty_bst) == 0, "Empty BST size should be 0"
    assert empty_bst.find_min() is None, "Empty BST min should be None"
    assert empty_bst.search(10) == False, "Search in empty BST should return False"
    
    # Single node BST
    single_bst = BinarySearchTree()
    single_bst.insert(42)
    assert single_bst.find_min() == 42, "Single node min failed"
    assert single_bst.find_max() == 42, "Single node max failed"
    assert single_bst.height() == 0, "Single node height should be 0"
    
    print("\n" + "=" * 50)
    print("All tests passed! ✅")


def interactive_demo():
    """Interactive demonstration of Binary Search Tree."""
    print("\nInteractive Binary Search Tree Demo")
    print("=" * 40)
    
    bst = BinarySearchTree()
    
    while True:
        print("\nChoose an operation:")
        print("1. Insert value")
        print("2. Search value")
        print("3. Delete value")
        print("4. Display tree")
        print("5. Show traversals")
        print("6. Show tree statistics")
        print("7. Exit")
        
        try:
            choice = input("Enter choice (1-7): ").strip()
            
            if choice == '1':
                value = int(input("Enter value to insert: "))
                if bst.insert(value):
                    print(f"✅ Inserted {value}")
                else:
                    print(f"❌ {value} already exists")
            
            elif choice == '2':
                value = int(input("Enter value to search: "))
                if bst.search(value):
                    print(f"✅ {value} found in tree")
                else:
                    print(f"❌ {value} not found")
            
            elif choice == '3':
                value = int(input("Enter value to delete: "))
                if bst.delete(value):
                    print(f"✅ Deleted {value}")
                else:
                    print(f"❌ {value} not found")
            
            elif choice == '4':
                bst.display_tree()
            
            elif choice == '5':
                print(f"Inorder:    {bst.inorder_traversal()}")
                print(f"Preorder:   {bst.preorder_traversal()}")
                print(f"Postorder:  {bst.postorder_traversal()}")
                print(f"Level-order: {bst.level_order_traversal()}")
            
            elif choice == '6':
                print(f"Size: {len(bst)}")
                print(f"Height: {bst.height()}")
                print(f"Min value: {bst.find_min()}")
                print(f"Max value: {bst.find_max()}")
                print(f"Is valid BST: {bst.is_valid_bst()}")
            
            elif choice == '7':
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter 1-7.")
        
        except ValueError:
            print("Please enter a valid integer.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Run comprehensive tests
    test_binary_search_tree()
    
    # Demonstrate with example
    print("\n" + "=" * 60)
    print("DEMONSTRATION: Building a BST")
    print("=" * 60)
    
    # Create example BST
    demo_bst = BinarySearchTree()
    demo_values = [15, 10, 20, 8, 12, 17, 25, 6, 11, 13, 27]
    
    print(f"Inserting values: {demo_values}")
    for val in demo_values:
        demo_bst.insert(val)
    
    print("\nFinal tree structure:")
    demo_bst.display_tree()
    
    print(f"\nSorted values (inorder): {demo_bst.inorder_traversal()}")
    print(f"Tree height: {demo_bst.height()}")
    print(f"Tree size: {len(demo_bst)}")
    
    # Optional: Run interactive demo
    # Uncomment the line below to try the interactive version
    # interactive_demo()