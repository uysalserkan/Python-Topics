#%% Snippet 1
def all_unique(lst):
    # Checking for uniqueness
    # The next method checks if there are duplicate items in the given list.
    # It uses a property set()that removes duplicate items from the list:
    return len(lst) == len(set(lst))


#%% Snippet 2
from collections import Counter


def anagram(first, second):
    # Anagram
    # This method can be used to check if two strings are anagrams.
    # An Anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    # usually using all the original letters exactly once:
    return Counter(first) == Counter(second)


#%% Snippet 3
# Memory
# And this can be used to check the memory usage of an object:

import sys

variable = 30
print(sys.getsizeof(variable))  # 24

#%% Snippet 4


def byte_size(string):
    # Size in Bytes
    # The method returns the length of the string in bytes:
    return (len(string.encode('utf-8')))


#%% Snippet 5
# This snippet can be used to output a string nonce without the need to use loops for this:
n = 2
s = "Programming"

print(s * n)
# ProgrammingProgramming

#%% Snippet 6

# And here is the register. The snippet uses a method
# title()to capitalize each word in a string:

s = "programming is awesome"

print(s.title())  # Programming Is Awesome

#%% Snippet 7
# This method splits the list into smaller lists of the specified size:


def chunk(list, size):
    return [list[i:i + size] for i in range(0, len(list), size)]


#%% Snippet 8
# So you remove the false values ( False, None, 0and «») from the list using filter():


def compact(lst):
    return list(filter(bool, lst))


compact([0, 1, False, 2, '', 3, 'a', 's', 34])  # [ 1, 2, 3, 'a', 's', 34 ]

#%% Snippet 9
# The following code can be used to transpose a 2D array:

array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
print(transposed)  # [('a', 'c', 'e'), ('b', 'd', 'f')]
#%% Snippet 10
# You can do multiple comparisons with all kinds of operators in one line:

a = 3
print(2 < a < 8)  # True
print(1 == a < 2)  # False
#%% Snippet 11
# The following snippet can be used to convert a list of strings to a single string,
# where each item from the list is separated by commas:

hobbies = ["singing", "soccer", "swimming"]

print("My hobbies are:")  # My hobbies are:
print(", ".join(hobbies))  # singing, soccer, swimming
#%% Snippet 12
# This method counts the number of vowels (“a”, “e”, “i”, “o”, “u”) found in the string:

import re


def count_vowels(str):
    return len(len(re.findall(r'[aeiou]', str, re.IGNORECASE)))


count_vowels('foobar')  # 3
count_vowels('gym')  # 0
#%% Snippet 13
# Use to convert the first letter of your specified string to lowercase:


def decapitalize(string):
    return string[:1].lower() + string[1:]


#%% Snippet 14
# The following methods flatten out a potentially deep list using recursion:


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def deep_flatten(xs):
    flat_list = []
    [flat_list.extend(deep_flatten(x))
     for x in xs] if isinstance(xs, list) else flat_list.append(xs)
    return flat_list


deep_flatten([1, [2], [[3], 4], 5])  # [1,2,3,4,5]

#%% Snippet 15
# The method finds the difference between the two iterations,
# keeping only the values ​​that are in the first:


def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)


difference([1, 2, 3], [1, 2, 4])  # [3]
#%% Snippet 16
# The following method returns the difference between
# the two lists after applying this function to each element of both lists:


def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


from math import floor
difference_by([2.1, 1.2], [2.3, 3.4], floor)  # [1.2]
difference_by([{
    'x': 2
}, {
    'x': 1
}], [{
    'x': 1
}], lambda v: v['x'])  # [ { x: 2 } ]

#%% Snippet 17
# You can call multiple functions on one line:


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


a, b = 4, 5
print((subtract if a > b else add)(a, b))  # 9

#%% Snippet 18
# This code checks to see if there are duplicate values ​​in the list using the fact
# that set()it only contains unique values:


def has_duplicates(lst):
    return len(lst) != len(set(lst))


x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x)  # True
has_duplicates(y)  # False
#%% Snippet 19
# The following method can be used to combine two dictionaries:


def merge_dictionaries(a, b):
    return {**a, **b}


a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_dictionaries(a, b))  # {'y': 3, 'x': 1, 'z': 4}

#%% Snippet 20
# Now let’s get down to converting two lists into a dictionary:


def to_dictionary(keys, values):
    return dict(zip(keys, values))


keys = ["a", "b", "c"]
values = [2, 3, 4]
print(to_dictionary(keys, values))  # {'a': 2, 'c': 4, 'b': 3}

#%% Snippet 21
# The snippet shows what you can use
# enumerate()to get both values ​​and indices of lists:

list = ["a", "b", "c", "d"]
for index, element in enumerate(list):
    print(
        "Value",
        element,
        "Index ",
        index,
    )

xy = enumerate(list)
print(type(xy))
#%% Snippet 22
# The following snippet shows how to write a
# simple calculator without the need for conditions if-else:

import operator
action = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": pow
}

print(action['-'](50, 25))  # 25
#%% Snippet 23
# Use to calculate the time it takes for a specific code to run:

import time

start_time = time.time()

a = 1
b = 2
c = a + b
print(c)  #3

end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)

#%% Snippet 24
# You can use elseas part of a block try:

try:
    2 * 3
    print("Try done")
except TypeError:
    print("Exception occured")
else:
    print("There were no exceptions")
#%% Snippet 25
# This method returns the most frequent item that appears in the list:


def most_frequent(list):
    return max(set(list), key=list.count)


numbers = [1, 2, 1, 2, 3, 2, 1, 4, 2]
most_frequent(numbers)
#%% Snippet 26
# The method checks if the given string is a palindrome:


def palindrome(a):
    return a == a[::-1]


palindrome('mom')  # True
palindrome('xaxax')
palindrome('saxaxaxaxs')
#%% Snippet 27
# This code can be used to randomize the order of items in a list.
# Note that shuffleworks in place and returns None:

from random import shuffle

foo = [1, 2, 3, 4]
shuffle(foo)
print(foo)  # [1, 4, 3, 2] , foo = [1, 2, 3, 4]
#%% Snippet 28
# A really quick way to swap two variables without the need for an extra one:


def swap(a, b):
    return b, a


a, b = -1, 14
swap(a, b)  # (14, -1)
#%% Snippet 29
# The code shows how you can get the default value
# if the key you are looking for is not included in the dictionary:

d = {'a': 1, 'b': 2}

print(d.get('a', 3))  # 1
print(d.get('c', 3))  # 3

# %%
