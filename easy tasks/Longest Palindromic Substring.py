def cl(a):
    if a==a[::-1]:
        return f"this is palindrome"
    return f'not palindrome'
s = str(input())
ass = s.lower()
a = "".join(char for char in ass if char.isalnum())
lw= cl(a)
print(lw)
# a =cl(s)
# print(a)