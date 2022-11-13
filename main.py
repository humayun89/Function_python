# function define:
input_1 = 10  ## Don't modify this
input_2 = 40  ## Don't modify this.

## TODO:
## Implement a function called sum_fun  that takes two inputs and returns their sum.
def sum_fun(input_1, input_2):
    return input_1 + input_2
result_sum=sum_fun(input_1,input_2)
print(result_sum)

# multiplication using define function:result_sum = sum_fun(input_1, input_2)

x=500
y= 200
def multiply(x,y):
    return x*y
result=multiply(x,y)
print(result)
# faw
students_names = ["Micheal Ford", "John Buch", "Isra Raul", "Messi Ronaldo"]

students_grades = [80, 53, 90, 100]


def link_names_grades(students_names, students_grades):
    names_grades = {}
    for x, y in zip(students_names, students_grades):
        names_grades[x] = y
    return names_grades.append
students_names = [ "Micheal Ford", "John Buch" , "Isra Raul", "Messi Ronaldo"]

students_grades = [ 80 , 53 , 90 , 100]
# Comprehensive lists:
## Don't modify this
students_names = [ "Micheal Ford", "John Buch" , "Isra Raul", "Messi Ronaldo"]

students_grades = [ 80 , 53 , 90 , 100]

def link_names_grades(students_names , students_grades ):
    names_grades = {}
    for x , y in zip(students_names , students_grades):
        names_grades[x] = y
    return names_grades
    print(names_grades)
##Newbie

numbers = [10, 20 , 17 , 13 ]
even_or_odd = True
filtered_list={}
numbers = [10, 20 , 17 , 13 ]
even_or_odd = True
filtered_list={}
def filter_even_odd(numbers,even_or_odd):
    for x ,y in zip (numbers,even_or_odd):
        if even_or_odd==False:
            print("EVEN")
        elif even_or_odd==True:
            print("ODD")
# Variable Scope :
