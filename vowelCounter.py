#! python3
# Program to count vowel letters from user's input

vowel = 'aeiou'
s = input(str('Enter a word:'))

count = 0
for i in s:
    if i in vowel:
        count += 1

print('Number of vowels: %s' %count)