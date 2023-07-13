print("important chinese proverb")

name = "John Smith"
age = 20
isNew = True

#inputs
    # getName = input("What is your name? ")
    # getFavColor = input("What's your favourite color? ")
    # print(getName + " likes " + getFavColor)

#strings
doubleS = "Sesame street 'excellent book'"
multipleLines = ''' 
oh how I miss my boys
my dear boys
always in trouble
'''
# [0:1] FROM INDEX : TO INDEX 
# assumed 0 -> 0:5 / output: JOHN
slicedName = name[:5]
# assumed 0 -> 5:0 / output SMITH
slicedSurname = name[5:]

# formatted string / template literals
formattedFullName = f'{slicedName}[{slicedSurname}] is not real'
print(formattedFullName)
