# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
#     - *Input*: [("John", 25), ("Jane", 30)]
#     - *Output*: "John is 25 years old. Jane is 30 years old."

details = [("John", 25), ("Jane", 30)]

print(details[0][0],"is",details[0][1],"years old.",details[1][0],"is",details[1][1],"years old.")

# 2. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"

def addnewagepair(name,age,details) :
    details.update({name:age})
    return details

def updatenameagepair(name,updatedage,details) :
    if name in details :
        details[name]=updatedage
        return details
    else :
        return "key doesn't exist"
    
def deletenameagepair(name,details):
    if name in details :
        del details[name]
        return details
    else :
        return "key doesn't exist"

my_dict={}
add=addnewagepair('John',25,my_dict)
print(add)
update = updatenameagepair("John",26,my_dict)
print(update)
delete = deletenameagepair("John",my_dict)
print(delete)


# 3. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"

array = [2, 7, 11, 15]
target = 9

def twoSum(arr,k) :
    for i in range (0,len(arr)) :
        for j in range (0,len(arr)) :
            if arr[i] == arr[j] :
                continue
            elif arr[i] + arr[j] == k :
                return [i,j]


result = twoSum(array,target)
print(result)


# 4. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

palin='madam'

def findPalindrome(str) :
    if str[::-1] == str :
        return True
    else:
        return False
    

res = findPalindrome(palin)

if res :
    print("The word",palin,"is a palindrome.")
else :
    print ("The word",palin,"isn't a Palindrome")



# 5. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"

def selectionSort(numbers) :

    for i in range (0,len(numbers)-1):
        min_index=i
        for j in range (i+1,len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index=j
            
        temp = numbers[i]
        numbers[i]= numbers[min_index]
        numbers[min_index]=temp

    return numbers

sortedlist = selectionSort([64, 25, 12, 22, 11])
print(sortedlist)

# 6. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"

# 7. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
#     - *Input*: None
#     - *Output*: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,..."

result = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        result.append('FizzBuzz')
    elif i % 3 == 0:
        result.append('Fizz')
    elif i % 5 == 0:
        result.append('Buzz')
    else:
        result.append(str(i))

print(", ".join(result))


# 8. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"

file = open("input.txt","r")
content = file.read()
file.close()
outputfile = open("./output.txt","w")
wordsCount = len(content.split())
outputfile.write ("Number of words:"+ str(wordsCount)+"\n")
outputfile.close()

# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."

def divisible(a,b) :
    try:
        c=int(a)/int(b)
        return (c)
    except :
        return "Cannot divide by zero."


print(divisible(10,5))

