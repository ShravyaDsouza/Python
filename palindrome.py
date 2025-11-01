def is_palindrome(str):
    str = str.lower()
    return str == str[::-1]

print(is_palindrome(""))