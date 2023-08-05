# 1. **Hello, World!**: Write a Python program that prints "Hello, World!" to the console.
#     - *Input*: None
#     - *Output*: "Hello, World!"
print("Hello, World!")

#2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
    # - *Input*: None
    # - *Output*: "Type of variable1: <class 'int'>, value: 10..."

variable1 = 4 #int
variable2 = 4.654 #float
variable3 = True #boolean
variable4 = [1,False,6.89,"shiva"] #list
variable5 = (1,2.34,"apple",True) #tuple
variable6 = {"number": 3, "float_num":5.67,"boolean":True} #dictionaries
variable7 = {1,2,4,3,2,2,5} #set

print("Type of variable1: ", type(variable1) ," value: ", variable1)
print("Type of variable2: ", type(variable2) ," value: ", variable2)
print("Type of variable3: ", type(variable3) ," value: ", variable3)
print("Type of variable4: ", type(variable4) ," value: ", variable4)
print("Type of variable5: ", type(variable5) ," value: ", variable5)
print("Type of variable6: ", type(variable6) ," value: ", variable6)
print("Type of variable7: ", type(variable7) ," value: ", variable7)


# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."

my_list = [1,2,3,4,5,6,7,8,9,20]


# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"

input =  [10, 20, 30, 40]
sum=0
for num in input :
    sum+=num

average = sum/len(input)
print("Sum: ",sum," Average: ",average)



# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"

def reverseAString(str) :
    reverseStr =""
    for i in range ( len( str )-1,-1,-1):
        reverseStr += str[i]
    return reverseStr
    
string = "Python"
result = reverseAString(string)
print(result)




# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

string = "Hello"
countVowel = 0
vowels="aeiouAEIOU"
for char in string :
    if char not in vowels :
        continue
    else :
        countVowel += 1
       
        
print("Number of vowels: ",countVowel)

# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."

def primeNumber(num) :
    count=0
    for i in range(2,num):
        if num%i== 0 :
            count+=1
    
    if count == 0 :
        return True
    else :
        return False

ans = primeNumber(13)
if ans :
    print(num,' is a prime number.')
else :
     print(num,' is not a prime number.')


# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

num=5

def factorialOfANumber(num) :
    ans=1
    for i in range(num,0,-1) :
        ans*=i
    print(ans)


# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"

my_fibanoacci = []
num=5
def fiboanacciFunc(num):
    for i in range (0,num) :
        my_fibanoacci.append(findFibNum(i))

def findFibNum(n) :
    if n == 0 :
        return 0
    elif n==1 or n==2:
        return 1
    

    
    return findFibNum(n-1)+findFibNum(n-2)

fiboanacciFunc(num)
print(my_fibanoacci)

# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"

my_list = []
for i in range(1,11) :
    my_list.append(i**2)

print(my_list)