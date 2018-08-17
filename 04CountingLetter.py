#counting a letter in string

str1 = 'the quick brown fox jumps over the lazy dog'
count = 0
f = input('Enter a letter: ')

for i in str1:
    if f == i :
        count += 1

print(f,'is present', count, 'times.')
    
    
