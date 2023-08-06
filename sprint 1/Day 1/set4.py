# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"

str1= "cinema"
str2= "iceman"

def is_anagram(s1,s2):
    s1 = sorted(s1)
    s2 = sorted(s2)

    return s1 == s2

print(is_anagram(str1,str2))

# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
#     - *Input*: [64, 34, 25, 12, 22, 11, 90]
#     - *Output*: "[11, 12, 22, 25, 34, 64, 90]"

unsortlist = [64, 34, 25, 12, 22, 11, 90]

def bubbleSort(arr) :
    n = len(arr)
    for i in range (0,n-1) :
        for j in range (0,n-1-i):
            if arr[j] > arr[j+1] :
                temp = arr[j]
                arr[j]= arr[j + 1]
                arr[j+1]=temp

    return arr

print(bubbleSort(unsortlist))


# 3. **Longest Common Prefix**: Given a list of strings, find the longest common prefix.
#     - *Input*: ["flower","flow","flight"]
#     - *Output*: "fl"

def checkPrefix(str1,str2) :
    long = ''
    i=0
    j=0
    while i<len(str1) and j<len(str2) :
        if str1[i] == str2[j]:
            long+=str1[i]
        else:
            break

        i+=1
        j+=1

    return long

stringslist = ["flower","flow","flow"]
long=stringslist[0]
for i in stringslist:
    if i[0] != long[0]:
        print("No prefixes")
        break
    else:
        long = checkPrefix(long, i)

print(long)


# 4. **String Permutations**: Write a Python function to calculate all permutations of a given string.
#     - *Input*: "abc"
#     - *Output*: "['abc', 'acb', 'bac', 'bca', 'cab', 'cba']"


def swap(string, i, j):
    string_list = list(string)
    temp = string_list[i]
    string_list[i] = string_list[j]
    string_list[j] = temp

    return ''.join(string_list)

def permutation(string, l):
    if l >= len(string) :
        result.append(string)

    i = l
    while i < len(string):
        string = swap(string, i, l)
        l += 1
        permutation(string, l)
        string = swap(string, i, l - 1)  # Note: We revert back to l - 1 here
        i += 1

string = "abc"
stringslist = []
for i in string:
    stringslist.append(i)

result = []
permutation(string, 0)
print(result)


# 6. **Missing Number**: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#     - *Input*: [3, 0, 1]
#     - *Output*: "2"

numbers = [3, 0, 1,2,5]
numbers = sorted(numbers)

for i in range (len(numbers)-1) :
    if numbers[i+1]-numbers[i] == 2:
        print(numbers[i]+1)
        break



# 7. **limbing Stairs**: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#     - *Input*: 3
#     - *Output*: "3"





# 8. **Invert Binary Tree**: Invert a binary tree (mirroring it).
#     - *Input*: A binary tree
#     - *Output*: Inverted binary tree




# 9. **Power of Two**: Given an integer, write a function to determine if it is a power of two.
#     - *Input*: 16
#     - *Output*: "True"

def findPowerOfTwo(n,i):
    if 2**i == n :
        return True
    elif 2**i>16 :
        return False
    
    return findPowerOfTwo(n,i+1)

n=16
print(findPowerOfTwo(n,1))



# 10. **Contains Duplicate**: Given an array of integers, find if the array contains any duplicates.
#     - *Input*: [1, 2, 3, 1]
#     - *Output*: "True"
numbers= [1, 2, 3, 1]
dup = {}

for i in numbers :
    if i in dup :
        dup[i]+=1
    else:
        dup[i]=1

def checkduplicates(dup):
    for key,value in dup.items() :
        if value > 1 :
            return True
        else:
            return False

print(checkduplicates(dup))


# 11. **Binary Search**: Write a function that implements binary search on a sorted array.
#     - *Input*: [1, 2, 3, 4, 5, 6], target = 4
#     - *Output*: "3"

import math
input11 = [1, 2, 3, 4, 5, 6]
target = 4
l=0
h=len(input11)-1

while l <= h :
    mid = math.floor(l+((h-l)/2))
    if input11[mid] == target :
        print(mid)
        break
    elif input11[mid] < target :
        l = mid + 1
    else :
        h = mid - 1





# 12. **Depth First Search (DFS)**: Implement DFS for a graph in Python.
#     - *Input*: A graph
#     - *Output*: Vertices visited in DFS order

def dfs(graph, node, visited):
    # Mark the current node as visited
    visited[node] = True
    print(node, end=' ')

    # Recur for all the neighbors of the current node
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}
# Initialize the visited dictionary with all nodes marked as False
visited = {node: False for node in graph}

# Call DFS starting from node 'A'
dfs(graph, 'A', visited)

print('-------------------------------------')

# 13. **Breadth First Search (BFS)**: Implement BFS for a graph in Python.
#     - *Input*: A graph
#     - *Output*: Vertices visited in BFS order

from collections import deque

def bfs(graph, start_node):
    visited = {node: False for node in graph}
    queue = deque([start_node])

    visited[start_node] = True

    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')

        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

# Call BFS starting from node 'A'
bfs(graph, 'A')

print('-------------------------------------')
# 14. **Quick Sort**: Implement quick sort in Python.
#     - *Input*: [10, 7, 8, 9, 1, 5]
#     - *Output*: "[1, 5, 7, 8, 9, 10]"

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example Input
input_array = [10, 7, 8, 9, 1, 5]

# Call Quick Sort
output_array = quick_sort(input_array)
print(output_array)
print('-------------------------------------')

# 15. **Single Number**: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#     - *Input*: [4,1,2,1,2]
#     - *Output*: "4"

non = [4,1,2,1,2]
elem_dict = {}
for i in non :
    if i in elem_dict :
        elem_dict[i]+=1
    else:
        elem_dict[i]=1

for key,value in elem_dict.items() :
    if value == 1 :
        print(key)
        

# 16. **Palindrome Linked List**: Given a singly linked list, determine if it is a palindrome.
#     - *Input*: [1,2,2,1]
#     - *Output*: "True"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    values = []
    current = head

    while current is not None:
        values.append(current.val)
        current = current.next

    return values == values[::-1]

def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

input_list = [1, 2, 2, 1]
linked_list = create_linked_list(input_list)

output = is_palindrome(linked_list)
print(output)  


# 17. **Implement Trie (Prefix Tree)**: Implement a trie with insert, search, and startsWith methods.
#     - *Input*: insert("apple"), search("apple"), startsWith("app")
#     - *Output*: "True, True"

# 18. **Maximum Subarray**: Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#     - *Input*: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#     - *Output*: "6"

def max_subarray_sum(nums):
    max_sum = float('-inf')  
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

input_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

output = max_subarray_sum(input_array)
print(output)  



# 19. **Implement Stack using Linked List**: Use Python's linked list data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"

# 20. **Basic Django Web App**: Create a basic web application using Django that has two routes, one that displays "Hello, World!" and one that displays "Goodbye, World!".
#     - *Input*: Visit "/", Visit "/goodbye"
#     - *Output*: "Hello, World!", "Goodbye, World!"