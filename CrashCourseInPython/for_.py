# for loop (long-form)
squares = []
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)

# use "list comprehension" to shorten for loop

# list comprehension 1
squares =[value**2 for value in range(1,11)]
print(squares)

# list comprehension 2
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(word_lengths)