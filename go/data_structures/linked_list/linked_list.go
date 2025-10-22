/*
Linked List Implementation in Go
===============================

Data Structure Description:
A Linked List is a linear data structure where elements are stored in nodes.
Each node contains data and a pointer to the next node. Unlike arrays, linked
lists don't require contiguous memory allocation.

Time Complexities:
- Insert at beginning: O(1)
- Insert at end: O(n)
- Delete: O(n)
- Search: O(n)

Space Complexity: O(n)

Applications:
- Dynamic memory allocation
- Implementation of stacks and queues
- Polynomial arithmetic
- Undo functionality in applications
*/

package main

import "fmt"

// Node represents a single node in the linked list
type Node struct {
	Data int
	Next *Node
}

// LinkedList represents the linked list structure
type LinkedList struct {
	Head *Node
	Size int
}

// NewLinkedList creates a new empty linked list
func NewLinkedList() *LinkedList {
	return &LinkedList{
		Head: nil,
		Size: 0,
	}
}

// IsEmpty checks if the linked list is empty
func (ll *LinkedList) IsEmpty() bool {
	return ll.Head == nil
}

// Length returns the number of nodes in the list
func (ll *LinkedList) Length() int {
	return ll.Size
}

// Prepend adds a new node at the beginning
func (ll *LinkedList) Prepend(data int) {
	newNode := &Node{Data: data, Next: ll.Head}
	ll.Head = newNode
	ll.Size++
}

// Append adds a new node at the end
func (ll *LinkedList) Append(data int) {
	newNode := &Node{Data: data, Next: nil}

	if ll.IsEmpty() {
		ll.Head = newNode
	} else {
		current := ll.Head
		for current.Next != nil {
			current = current.Next
		}
		current.Next = newNode
	}
	ll.Size++
}

// InsertAt inserts a new node at a specific position
func (ll *LinkedList) InsertAt(data, position int) error {
	if position < 0 || position > ll.Size {
		return fmt.Errorf("invalid position: %d", position)
	}

	if position == 0 {
		ll.Prepend(data)
		return nil
	}

	newNode := &Node{Data: data}
	current := ll.Head

	for i := 0; i < position-1; i++ {
		current = current.Next
	}

	newNode.Next = current.Next
	current.Next = newNode
	ll.Size++

	return nil
}

// DeleteFirst removes the first node
func (ll *LinkedList) DeleteFirst() (int, error) {
	if ll.IsEmpty() {
		return 0, fmt.Errorf("cannot delete from empty list")
	}

	data := ll.Head.Data
	ll.Head = ll.Head.Next
	ll.Size--

	return data, nil
}

// DeleteLast removes the last node
func (ll *LinkedList) DeleteLast() (int, error) {
	if ll.IsEmpty() {
		return 0, fmt.Errorf("cannot delete from empty list")
	}

	if ll.Head.Next == nil {
		data := ll.Head.Data
		ll.Head = nil
		ll.Size--
		return data, nil
	}

	current := ll.Head
	for current.Next.Next != nil {
		current = current.Next
	}

	data := current.Next.Data
	current.Next = nil
	ll.Size--

	return data, nil
}

// DeleteAt removes a node at a specific position
func (ll *LinkedList) DeleteAt(position int) (int, error) {
	if position < 0 || position >= ll.Size {
		return 0, fmt.Errorf("invalid position: %d", position)
	}

	if position == 0 {
		return ll.DeleteFirst()
	}

	current := ll.Head
	for i := 0; i < position-1; i++ {
		current = current.Next
	}

	data := current.Next.Data
	current.Next = current.Next.Next
	ll.Size--

	return data, nil
}

// DeleteByValue removes the first node with the specified value
func (ll *LinkedList) DeleteByValue(value int) bool {
	if ll.IsEmpty() {
		return false
	}

	if ll.Head.Data == value {
		ll.DeleteFirst()
		return true
	}

	current := ll.Head
	for current.Next != nil {
		if current.Next.Data == value {
			current.Next = current.Next.Next
			ll.Size--
			return true
		}
		current = current.Next
	}

	return false
}

// Search finds the index of a value in the list
func (ll *LinkedList) Search(value int) int {
	current := ll.Head
	index := 0

	for current != nil {
		if current.Data == value {
			return index
		}
		current = current.Next
		index++
	}

	return -1
}

// Get returns the value at a specific position
func (ll *LinkedList) Get(position int) (int, error) {
	if position < 0 || position >= ll.Size {
		return 0, fmt.Errorf("invalid position: %d", position)
	}

	current := ll.Head
	for i := 0; i < position; i++ {
		current = current.Next
	}

	return current.Data, nil
}

// Reverse reverses the linked list in-place
func (ll *LinkedList) Reverse() {
	var prev *Node
	current := ll.Head

	for current != nil {
		nextNode := current.Next
		current.Next = prev
		prev = current
		current = nextNode
	}

	ll.Head = prev
}

// FindMiddle returns the middle element using slow-fast pointer technique
func (ll *LinkedList) FindMiddle() (int, error) {
	if ll.IsEmpty() {
		return 0, fmt.Errorf("list is empty")
	}

	slow := ll.Head
	fast := ll.Head

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	return slow.Data, nil
}

// HasCycle detects if the list has a cycle using Floyd's algorithm
func (ll *LinkedList) HasCycle() bool {
	if ll.IsEmpty() {
		return false
	}

	slow := ll.Head
	fast := ll.Head

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next

		if slow == fast {
			return true
		}
	}

	return false
}

// RemoveDuplicates removes duplicate values from the list
func (ll *LinkedList) RemoveDuplicates() {
	if ll.IsEmpty() {
		return
	}

	seen := make(map[int]bool)
	current := ll.Head
	seen[current.Data] = true

	for current.Next != nil {
		if seen[current.Next.Data] {
			current.Next = current.Next.Next
			ll.Size--
		} else {
			seen[current.Next.Data] = true
			current = current.Next
		}
	}
}

// ToSlice converts the linked list to a slice
func (ll *LinkedList) ToSlice() []int {
	result := make([]int, 0, ll.Size)
	current := ll.Head

	for current != nil {
		result = append(result, current.Data)
		current = current.Next
	}

	return result
}

// Print displays the linked list
func (ll *LinkedList) Print() {
	if ll.IsEmpty() {
		fmt.Println("Empty List")
		return
	}

	current := ll.Head
	for current != nil {
		fmt.Printf("%d", current.Data)
		if current.Next != nil {
			fmt.Print(" -> ")
		}
		current = current.Next
	}
	fmt.Println(" -> nil")
}

// Clear removes all nodes from the list
func (ll *LinkedList) Clear() {
	ll.Head = nil
	ll.Size = 0
}

// TestLinkedList runs comprehensive tests
func TestLinkedList() {
	fmt.Println("Testing Linked List Implementation")
	fmt.Println(string(make([]byte, 50)))

	// Test 1: Basic operations
	fmt.Println("\nTest 1: Basic Operations")
	ll := NewLinkedList()

	if !ll.IsEmpty() {
		panic("New list should be empty")
	}

	ll.Append(1)
	ll.Append(2)
	ll.Append(3)

	fmt.Printf("After appending 1, 2, 3: ")
	ll.Print()

	if ll.Length() != 3 {
		panic("Size should be 3")
	}
	fmt.Println("Test passed ✓")

	// Test 2: Prepend
	fmt.Println("\nTest 2: Prepend Operation")
	ll.Prepend(0)
	fmt.Printf("After prepending 0: ")
	ll.Print()

	expected := []int{0, 1, 2, 3}
	if !sliceEqual(ll.ToSlice(), expected) {
		panic("Prepend failed")
	}
	fmt.Println("Test passed ✓")

	// Test 3: Insert at position
	fmt.Println("\nTest 3: Insert at Position")
	ll.InsertAt(99, 2)
	fmt.Printf("After inserting 99 at position 2: ")
	ll.Print()

	if val, _ := ll.Get(2); val != 99 {
		panic("Insert at position failed")
	}
	fmt.Println("Test passed ✓")

	// Test 4: Search
	fmt.Println("\nTest 4: Search Operation")
	index := ll.Search(99)
	fmt.Printf("Index of value 99: %d\n", index)

	if index != 2 {
		panic("Search failed")
	}
	fmt.Println("Test passed ✓")

	// Test 5: Delete operations
	fmt.Println("\nTest 5: Delete Operations")
	ll.DeleteFirst()
	fmt.Printf("After deleting first: ")
	ll.Print()

	ll.DeleteLast()
	fmt.Printf("After deleting last: ")
	ll.Print()

	ll.DeleteAt(1)
	fmt.Printf("After deleting at position 1: ")
	ll.Print()
	fmt.Println("Test passed ✓")

	// Test 6: Reverse
	fmt.Println("\nTest 6: Reverse Operation")
	ll2 := NewLinkedList()
	for i := 1; i <= 5; i++ {
		ll2.Append(i)
	}
	fmt.Printf("Original: ")
	ll2.Print()

	ll2.Reverse()
	fmt.Printf("Reversed: ")
	ll2.Print()

	expectedReverse := []int{5, 4, 3, 2, 1}
	if !sliceEqual(ll2.ToSlice(), expectedReverse) {
		panic("Reverse failed")
	}
	fmt.Println("Test passed ✓")

	// Test 7: Find middle
	fmt.Println("\nTest 7: Find Middle Element")
	ll3 := NewLinkedList()
	for i := 1; i <= 5; i++ {
		ll3.Append(i)
	}
	fmt.Printf("List: ")
	ll3.Print()

	middle, _ := ll3.FindMiddle()
	fmt.Printf("Middle element: %d\n", middle)

	if middle != 3 {
		panic("Find middle failed")
	}
	fmt.Println("Test passed ✓")

	// Test 8: Remove duplicates
	fmt.Println("\nTest 8: Remove Duplicates")
	ll4 := NewLinkedList()
	values := []int{1, 2, 2, 3, 3, 3, 4, 5, 5}
	for _, v := range values {
		ll4.Append(v)
	}
	fmt.Printf("Before: ")
	ll4.Print()

	ll4.RemoveDuplicates()
	fmt.Printf("After:  ")
	ll4.Print()

	expectedUnique := []int{1, 2, 3, 4, 5}
	if !sliceEqual(ll4.ToSlice(), expectedUnique) {
		panic("Remove duplicates failed")
	}
	fmt.Println("Test passed ✓")

	// Test 9: Edge cases
	fmt.Println("\nTest 9: Edge Cases")
	emptyLL := NewLinkedList()

	_, err := emptyLL.DeleteFirst()
	if err == nil {
		panic("Should error on empty list delete")
	}

	singleLL := NewLinkedList()
	singleLL.Append(42)
	val, _ := singleLL.Get(0)

	if val != 42 {
		panic("Single element test failed")
	}
	fmt.Println("Test passed ✓")

	fmt.Println("\n" + string(make([]byte, 50)))
	fmt.Println("All tests passed! 🎉")
}

// Helper function
func sliceEqual(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

// Demonstration
func DemoLinkedList() {
	fmt.Println("\n" + string(make([]byte, 60)))
	fmt.Println("DEMONSTRATION: Linked List Applications")
	fmt.Println(string(make([]byte, 60)))

	// Demo 1: Building a list
	fmt.Println("\n1. Building a To-Do List:")
	todoList := NewLinkedList()

	tasks := []int{101, 102, 103, 104, 105}
	for _, task := range tasks {
		todoList.Append(task)
		fmt.Printf("Added task %d\n", task)
	}

	fmt.Printf("Current tasks: ")
	todoList.Print()

	// Demo 2: Manipulating the list
	fmt.Println("\n2. Completing Tasks:")
	completed, _ := todoList.DeleteFirst()
	fmt.Printf("Completed task %d\n", completed)
	fmt.Printf("Remaining tasks: ")
	todoList.Print()

	// Demo 3: Finding information
	fmt.Println("\n3. Finding Middle Task:")
	middle, _ := todoList.FindMiddle()
	fmt.Printf("Middle task ID: %d\n", middle)
}

func main() {
	// Run tests
	TestLinkedList()

	// Run demonstrations
	DemoLinkedList()
}
