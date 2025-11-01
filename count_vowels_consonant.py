def count_vowels_consonants(s):
    vowels = set("aeiou")
    v = c = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c

# Example
s = "A man, a plan, a canal: Panama! 123"
v, c = count_vowels_consonants(s)
print("Vowels:", v, "Consonants:", c)