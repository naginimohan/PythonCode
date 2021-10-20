str = input('enter string \n')
str1 = str.casefold()
revStr = reversed(str1)
if(list(str) == list(revStr)):
    print("It is palindrome")
else:
    print("it is not palindrome")    