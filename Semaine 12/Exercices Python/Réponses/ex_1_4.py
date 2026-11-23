# 1.4 Le palindrome magique
phrase = input('Phrase : ')
net = phrase.lower().replace(' ', '')
if net == net[::-1]:
    print('Palindrome magique !')
else:
    print("Ce n'est pas un palindrome.")
