# Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countDown(number):
    for i in range(number,0, -1):
        print(i)

countDown(15)

# Create a function that will receive a list with two numbers. Print the first value and return the second.

def twoNumbers(num1, num2):
    print(num1)
    return(num2)

result1=twoNumbers(5, 10)
print(result1)

#  Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def sumValue(list):
    sum=list[0]+len(list)
    return sum

result2=sumValue([10,5,3])
print(result2)

# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def createList(list):
    newList=[]
    for number in list():
        pass

result3=createList([5,10,20,30,50])
# Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.