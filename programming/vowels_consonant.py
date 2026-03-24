ch=input("enter any character:")
if "A"<=ch<="Z" or "a"<=ch<="z":
    if ch in "aeiouAEIOU":
        print("character is vowels")
    else:
        print("character is consonant")
else:
    print("other than alphabets")
