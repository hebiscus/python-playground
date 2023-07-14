print("important chinese proverb")

name = "John Smith"
age = 20
isNew = True

#inputs
    # getName = input("What is your name? ")
    # getFavColor = input("What's your favourite color? ")
    # print(getName + " likes " + getFavColor)

#strings | immutable
    # doubleS = "Sesame street 'excellent book'"
    # multipleLines = ''' 
    # oh how I miss my boys
    # my dear boys
    # always in trouble
    # '''
    # # [0:1] FROM INDEX : TO INDEX /  # characters from position 0 (included) to 5 (excluded)
    # # assumed 0 -> 0:5 / output: JOHN
    # slicedName = name[:5]
    # # assumed 0 -> 5:0 / output SMITH 
    # slicedSurname = name[5:]

    # # formatted string / template literals
    # formattedFullName = f'{slicedName}[{slicedSurname}] is not real'

    # # string methods: 
    # # .find (index of char); .replace; len(); lower(); upper(); .title()

# arithmetic operations
# 10 / 3 -> float
# 10 // 3 -> integer

# match statement = similar switch statement in sj

# list = [3, 1, -5, 100, 34]
# biggest = 0
# for number in list:
#     if number > biggest:
#         biggest = number
# print(biggest)

#  list mutable, tuple immutable 

# blaba = {
#     "name": "blaba",
#     "baba": "name"
# }

# print(blaba["name"]) or print(blaba.get("name"))

# classes 
class MyClass:
    # contructor
    def __init__(self, plant):
        self.data = [plant]

    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
# new instance
x = MyClass("roses") 
# ['roses']
print(x.data)

