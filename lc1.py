old_list =[10,20,30,40,50]
new_list=[]

#old way
for x in old_list:
    if x > 20:
        x += 20
        new_list.append(x)

print(new_list)

#using list comprehension
new_list = [x + 20 for x in old_list if x > 20]

print(new_list)


x = [i for i in range(10)]
print(x)

square = [i**2 for i in x]
print(square)

list1 = [3,4,5,]
multiplied = [item *3 for item in list1]
print(multiplied)

listofwords = ['this', 'is', 'a', 'list', 'of', 'words']
items = [i[0] for i  in listofwords]
print(items)

list1 = ['A', 'B','C']
list2 = [x.lower() for x in list1]
print(list2)

#squaring only even numbers from range 0-4
new_range = [i*i for i in range(5) if i % 2==0]
print(new_range)

#extract the numbers
string = 'Hello 12345 World'

numbers = [x for x in string if x.isdigit()]
print(numbers)

letters = [x for x in string if x.isalpha()]
print(letters)

#using a file to find
myfile = open('test.txt', 'r')
result = [i.rstrip('\n') for i in myfile if 'line3' in i]
print(result)

#using functions
def double(x):
    return x*2

print(double(10))

mynumbers = [double(x) for x in range(10)]
print(mynumbers)

#more than one list and argument

result = [x+y for x in [10,20,30] for y in [20,40,60]]
print(result)