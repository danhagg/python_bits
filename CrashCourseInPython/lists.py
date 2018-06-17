"""Here are some other common list methods.

list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
list.reverse() -- reverses the list in place (does not return it)
list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
Notice that these are *methods* on a list object, while len() is a function that takes the list (or string or whatever) as an argument.
"""
list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print (list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print (list.index('curly'))    ## 2

list.remove('curly')         ## search and remove that element
list.pop(1)                  ## removes and returns 'larry'
print (list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

squares = []
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

#list comprehension
#combines for loop and addition of elements as in ch4_1
squares_1 =[value**2 for value in range(1,11)]
print(squares_1)

#count to 20
twenty = [unit for unit in range(1,21)]
print(twenty)

#play with millions
million = [millionth for millionth in range(1,1000001)]
print(min(million))
print(max(million))
print(sum(million))

#odd 20
odds = [odd for odd in range(1,21,2)]
print(odds)

#3 to 30
threes = [three for three in range(3,33,3)]
print(threes)

#cubing
cubes = [cube**3 for cube in range(1,11)]
print(cubes)

#slicing from index 2 to 4
print(cubes[2:5])

#slicing between first and 4th(not including 4th)
print(cubes[:4])

#slicing to end
print(cubes[5:])

#slicing from end back
print(cubes[-3:])

#loop thru a slice
names = ['dan','mom','haitham','laith']
for name in names[-2:]:
    print(name.title())

#copy entire list
our_names = names[:]
print(our_names)

#list comprehension
squares =[value**2 for value in range(1,11)]
print(squares)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(word_lengths)
