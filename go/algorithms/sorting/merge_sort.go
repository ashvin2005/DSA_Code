/*
Merge Sort Algorithm Implementation in Go
========================================

Algorithm Description:
Merge Sort is a divide-and-conquer algorithm that divides the array into two halves,
recursively sorts them, and then merges the sorted halves back together.

Time Complexity: O(n log n) in all cases (best, average, worst)
Space Complexity: O(n) for temporary arrays
Stability: Stable (maintains relative order of equal elements)

Applications:
- External sorting (large datasets that don't fit in memory)
- Sorting linked lists efficiently
- Inversion counting
- Parallel processing (divide-and-conquer nature)
*/

package main

import (
	"fmt"
	"math/rand"
	"time"
)

// MergeSort sorts a slice of integers using merge sort algorithm
func MergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	// Create a copy to avoid modifying original
	result := make([]int, len(arr))
	copy(result, arr)

	mergeSortHelper(result, 0, len(result)-1)
	return result
}

// Helper function for recursive merge sort
func mergeSortHelper(arr []int, left, right int) {
	if left < right {
		mid := left + (right-left)/2

		// Recursively sort both halves
		mergeSortHelper(arr, left, mid)
		mergeSortHelper(arr, mid+1, right)

		// Merge the sorted halves
		merge(arr, left, mid, right)
	}
}

// merge combines two sorted subarrays into one sorted array
func merge(arr []int, left, mid, right int) {
	// Create temporary arrays
	leftSize := mid - left + 1
	rightSize := right - mid

	leftArr := make([]int, leftSize)
	rightArr := make([]int, rightSize)

	// Copy data to temporary arrays
	copy(leftArr, arr[left:mid+1])
	copy(rightArr, arr[mid+1:right+1])

	// Merge the temporary arrays back
	i, j, k := 0, 0, left

	for i < leftSize && j < rightSize {
		if leftArr[i] <= rightArr[j] {
			arr[k] = leftArr[i]
			i++
		} else {
			arr[k] = rightArr[j]
			j++
		}
		k++
	}

	// Copy remaining elements from left array
	for i < leftSize {
		arr[k] = leftArr[i]
		i++
		k++
	}

	// Copy remaining elements from right array
	for j < rightSize {
		arr[k] = rightArr[j]
		j++
		k++
	}
}

// MergeSortStrings sorts a slice of strings
func MergeSortStrings(arr []string) []string {
	if len(arr) <= 1 {
		return arr
	}

	result := make([]string, len(arr))
	copy(result, arr)

	mergeSortStringsHelper(result, 0, len(result)-1)
	return result
}

func mergeSortStringsHelper(arr []string, left, right int) {
	if left < right {
		mid := left + (right-left)/2
		mergeSortStringsHelper(arr, left, mid)
		mergeSortStringsHelper(arr, mid+1, right)
		mergeStrings(arr, left, mid, right)
	}
}

func mergeStrings(arr []string, left, mid, right int) {
	leftArr := make([]string, mid-left+1)
	rightArr := make([]string, right-mid)

	copy(leftArr, arr[left:mid+1])
	copy(rightArr, arr[mid+1:right+1])

	i, j, k := 0, 0, left

	for i < len(leftArr) && j < len(rightArr) {
		if leftArr[i] <= rightArr[j] {
			arr[k] = leftArr[i]
			i++
		} else {
			arr[k] = rightArr[j]
			j++
		}
		k++
	}

	for i < len(leftArr) {
		arr[k] = leftArr[i]
		i++
		k++
	}

	for j < len(rightArr) {
		arr[k] = rightArr[j]
		j++
		k++
	}
}

// CountInversions counts the number of inversions while sorting
// An inversion is a pair (i, j) where i < j but arr[i] > arr[j]
func CountInversions(arr []int) ([]int, int) {
	result := make([]int, len(arr))
	copy(result, arr)

	inversions := countInversionsHelper(result, 0, len(result)-1)
	return result, inversions
}

func countInversionsHelper(arr []int, left, right int) int {
	inversions := 0

	if left < right {
		mid := left + (right-left)/2

		inversions += countInversionsHelper(arr, left, mid)
		inversions += countInversionsHelper(arr, mid+1, right)
		inversions += mergeAndCount(arr, left, mid, right)
	}

	return inversions
}

func mergeAndCount(arr []int, left, mid, right int) int {
	leftArr := make([]int, mid-left+1)
	rightArr := make([]int, right-mid)

	copy(leftArr, arr[left:mid+1])
	copy(rightArr, arr[mid+1:right+1])

	i, j, k := 0, 0, left
	inversions := 0

	for i < len(leftArr) && j < len(rightArr) {
		if leftArr[i] <= rightArr[j] {
			arr[k] = leftArr[i]
			i++
		} else {
			arr[k] = rightArr[j]
			j++
			// All remaining elements in left array form inversions with rightArr[j]
			inversions += len(leftArr) - i
		}
		k++
	}

	for i < len(leftArr) {
		arr[k] = leftArr[i]
		i++
		k++
	}

	for j < len(rightArr) {
		arr[k] = rightArr[j]
		j++
		k++
	}

	return inversions
}

// MergeTwoSortedArrays merges two already sorted arrays
func MergeTwoSortedArrays(arr1, arr2 []int) []int {
	result := make([]int, len(arr1)+len(arr2))
	i, j, k := 0, 0, 0

	for i < len(arr1) && j < len(arr2) {
		if arr1[i] <= arr2[j] {
			result[k] = arr1[i]
			i++
		} else {
			result[k] = arr2[j]
			j++
		}
		k++
	}

	for i < len(arr1) {
		result[k] = arr1[i]
		i++
		k++
	}

	for j < len(arr2) {
		result[k] = arr2[j]
		j++
		k++
	}

	return result
}

// TestMergeSort runs comprehensive tests
func TestMergeSort() {
	fmt.Println("Testing Merge Sort Implementation")
	fmt.Println(string(make([]byte, 50)))

	// Test 1: Basic integer sorting
	fmt.Println("\nTest 1: Basic Integer Sorting")
	arr1 := []int{64, 34, 25, 12, 22, 11, 90}
	sorted1 := MergeSort(arr1)
	expected1 := []int{11, 12, 22, 25, 34, 64, 90}
	fmt.Printf("Input:    %v\n", arr1)
	fmt.Printf("Output:   %v\n", sorted1)
	fmt.Printf("Expected: %v\n", expected1)

	if !slicesEqual(sorted1, expected1) {
		panic("Test 1 failed")
	}
	fmt.Println("Test passed ✓")

	// Test 2: Already sorted
	fmt.Println("\nTest 2: Already Sorted Array")
	arr2 := []int{1, 2, 3, 4, 5}
	sorted2 := MergeSort(arr2)
	fmt.Printf("Input:  %v\n", arr2)
	fmt.Printf("Output: %v\n", sorted2)

	if !slicesEqual(sorted2, arr2) {
		panic("Test 2 failed")
	}
	fmt.Println("Test passed ✓")

	// Test 3: Reverse sorted
	fmt.Println("\nTest 3: Reverse Sorted Array")
	arr3 := []int{5, 4, 3, 2, 1}
	sorted3 := MergeSort(arr3)
	expected3 := []int{1, 2, 3, 4, 5}
	fmt.Printf("Input:  %v\n", arr3)
	fmt.Printf("Output: %v\n", sorted3)

	if !slicesEqual(sorted3, expected3) {
		panic("Test 3 failed")
	}
	fmt.Println("Test passed ✓")

	// Test 4: Array with duplicates
	fmt.Println("\nTest 4: Array with Duplicates")
	arr4 := []int{3, 1, 4, 1, 5, 9, 2, 6, 5, 3}
	sorted4 := MergeSort(arr4)
	fmt.Printf("Input:  %v\n", arr4)
	fmt.Printf("Output: %v\n", sorted4)

	if !isSorted(sorted4) {
		panic("Test 4 failed")
	}
	fmt.Println("Test passed ✓")

	// Test 5: String sorting
	fmt.Println("\nTest 5: String Sorting")
	strArr := []string{"banana", "apple", "cherry", "date"}
	sortedStr := MergeSortStrings(strArr)
	expectedStr := []string{"apple", "banana", "cherry", "date"}
	fmt.Printf("Input:    %v\n", strArr)
	fmt.Printf("Output:   %v\n", sortedStr)
	fmt.Printf("Expected: %v\n", expectedStr)

	if !stringSlicesEqual(sortedStr, expectedStr) {
		panic("Test 5 failed")
	}
	fmt.Println("Test passed ✓")

	// Test 6: Inversion counting
	fmt.Println("\nTest 6: Inversion Counting")
	arr6 := []int{2, 3, 8, 6, 1}
	sorted6, inversions := CountInversions(arr6)
	fmt.Printf("Input:      %v\n", arr6)
	fmt.Printf("Sorted:     %v\n", sorted6)
	fmt.Printf("Inversions: %d\n", inversions)

	if inversions != 5 {
		panic("Test 6 failed")
	}
	fmt.Println("Test passed ✓")

	// Test 7: Merge two sorted arrays
	fmt.Println("\nTest 7: Merge Two Sorted Arrays")
	arr7a := []int{1, 3, 5, 7}
	arr7b := []int{2, 4, 6, 8}
	merged := MergeTwoSortedArrays(arr7a, arr7b)
	expectedMerged := []int{1, 2, 3, 4, 5, 6, 7, 8}
	fmt.Printf("Array 1:  %v\n", arr7a)
	fmt.Printf("Array 2:  %v\n", arr7b)
	fmt.Printf("Merged:   %v\n", merged)

	if !slicesEqual(merged, expectedMerged) {
		panic("Test 7 failed")
	}
	fmt.Println("Test passed ✓")

	// Test 8: Edge cases
	fmt.Println("\nTest 8: Edge Cases")
	emptyArr := []int{}
	singleArr := []int{42}

	sortedEmpty := MergeSort(emptyArr)
	sortedSingle := MergeSort(singleArr)

	fmt.Printf("Empty array:  %v\n", sortedEmpty)
	fmt.Printf("Single element: %v\n", sortedSingle)

	if len(sortedEmpty) != 0 || len(sortedSingle) != 1 || sortedSingle[0] != 42 {
		panic("Test 8 failed")
	}
	fmt.Println("Test passed ✓")

	fmt.Println("\n" + string(make([]byte, 50)))
	fmt.Println("All tests passed! 🎉")
}

// Helper functions
func slicesEqual(a, b []int) bool {
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

func stringSlicesEqual(a, b []string) bool {
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

func isSorted(arr []int) bool {
	for i := 1; i < len(arr); i++ {
		if arr[i] < arr[i-1] {
			return false
		}
	}
	return true
}

// Demonstration
func DemoMergeSort() {
	fmt.Println("\n" + string(make([]byte, 60)))
	fmt.Println("DEMONSTRATION: Merge Sort Applications")
	fmt.Println(string(make([]byte, 60)))

	// Demo 1: Sorting student scores
	fmt.Println("\n1. Sorting Student Scores:")
	scores := []int{85, 72, 95, 68, 91, 78, 88}
	fmt.Printf("Unsorted scores: %v\n", scores)

	sortedScores := MergeSort(scores)
	fmt.Printf("Sorted scores:   %v\n", sortedScores)

	// Demo 2: Performance benchmark
	fmt.Println("\n2. Performance Benchmark:")
	sizes := []int{100, 1000, 10000}

	for _, size := range sizes {
		arr := make([]int, size)
		for i := range arr {
			arr[i] = rand.Intn(1000)
		}

		start := time.Now()
		MergeSort(arr)
		duration := time.Since(start)

		fmt.Printf("Sorted %d elements in %v\n", size, duration)
	}

	// Demo 3: Finding array disorder
	fmt.Println("\n3. Measuring Array Disorder (Inversions):")
	disorderedArr := []int{5, 4, 3, 2, 1}
	partiallyOrdered := []int{1, 3, 2, 4, 5}

	_, inv1 := CountInversions(disorderedArr)
	_, inv2 := CountInversions(partiallyOrdered)

	fmt.Printf("Completely reversed %v: %d inversions\n", disorderedArr, inv1)
	fmt.Printf("Partially ordered %v: %d inversions\n", partiallyOrdered, inv2)
}

func main() {
	// Seed random number generator
	rand.Seed(time.Now().UnixNano())

	// Run tests
	TestMergeSort()

	// Run demonstrations
	DemoMergeSort()
}
