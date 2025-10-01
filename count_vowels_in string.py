s=input("enter a string  ")
vowel_count=sum(1 for c in s.lower() if c in "aeiou")
print(vowel_count)