def disemvowel(word=None):
    word = input("Enter a word to be disemvoweled.\n==> ")
    word = list(word)
    x=0
    for a in range(len(word)):
        try:
            if word[x].lower() == 'a':
                del word[x]
                x-=1
            if word[x].lower() == 'e':
                del word[x]
                x-=1
            if word[x].lower() == 'i':
                del word[x]
                x-=1
            if word[x].lower() == 'o':
                del word[x]
                x-=1
            if word[x].lower() == 'u':
                del word[x]
                x-=1
        except IndexError:
            pass
        x+=1
    word = ''.join(word)
    return word

word = None
word = disemvowel(word)
print("What's left = " + word)