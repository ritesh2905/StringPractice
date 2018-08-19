'''
Write a Python program to count the number of characters (character frequency) in a string. Go to the editor 
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''
a = input('Enter: ')
a = list(a)

d = {}

for j in a:
    count = 0
    for k in a:
        if j == k:
            count += 1
        d[j] = count

print(d)
