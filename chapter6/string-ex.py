# name=input('Enter: ')
# print(type(name))
# print(name)


# ---------------------


# fruit = 'banana'
# letter = fruit[0]
# print(letter)
# letter = fruit[1]
# print(letter)
# letter = fruit[2]
# print(letter)

# IndexError: string index out of range
# letter = fruit[6]


# ---------------------


# fruit = 'apple'
# print(len(fruit))


# ---------------------


# fruit = 'banana'

# print('while loop')
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index += 1

# print('for loop')
# for letter in fruit:
#     print(letter)


# ---------------------


myString = 'Monty Python'
print(myString[0:4]) # Mont

print(myString[6:7]) # P

print(myString[6:20]) # Python

print(myString[:2]) # Mo

print(myString[8:]) # thon

print(myString[:]) # Monty Python


# ---------------------

firstString = 'Hello'
secondString = 'There'

print(firstString + secondString)  # HelloThere

thirdString = firstString + ' ' + secondString

print(thirdString) # Hello There


# ---------------------

fruit = 'banana'

print('n' in fruit) # True

print('m' in fruit) # False

print('nan' in fruit) # True

if 'a' in fruit:
    print('Found it!')

# ---------------------

greet = 'Hello Bob'
zap = greet.lower()
print(zap)

print(greet)

print(greet.upper())

# ---------------------

greet = '                Hello, Bob       '

print(greet.lstrip())

print(greet.rstrip())

print(greet.strip())

# ---------------------

line = 'Please have a nice day'
print(line.startswith('Please'))

print(line.startswith('p'))