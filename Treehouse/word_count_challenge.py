# word_count challenge
# Count how many of each word are in a phrase and output it as a dictionary

def word_count(phrase):
    phrase = phrase.lower()
    phrase_split = phrase.split(" ")
    words_count = []
    for x in range(len(phrase_split)):
        word = phrase_split[x]
        words_count.append(0)
        for words in phrase_split:
            if word == words:
                words_count[x] += 1 
        count[word] = words_count[x]
    return count

count = {}
phrase = input("What phrase do you want to word count?\n-> ")
word_count(phrase)
print(count)