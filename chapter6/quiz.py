words = 'Connect Foundation'
if 'F' in words:
    words.lower()
    # TypeError: 'str' object does not support item assignment 
    # => The reason for the error is that strings are immutable
    words[7] = '&' 
else:
    print(words)
print(words)
