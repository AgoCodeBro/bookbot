def main():

    with open("books/frankenstein.txt") as book:
        text = book.read()
        printWordCount(text)
        printCharFrequency(text)
        printReport(text)


def printWordCount(text):

        print(text)
        words = text.split()
        word_count = len(words)
        print(word_count)


def printCharFrequency(text):
    
    charCount = findCharFrequency(text)

    print(charCount)


def findCharFrequency(text):

    text = text.lower()
    charCount = {}
    for char in text:
        
        if char in charCount:

            charCount[char] += 1

        else:

            charCount[char] = 1

    return charCount


def sortedKeys(text):

    keys = []
    charCount = findCharFrequency(text)

    for key in charCount:

        if key.isalpha():

            keys.append(key)

    keys.sort()

    return keys


def printReport(text):

    keys = sortedKeys(text)
    charCount = findCharFrequency(text)
    print("---------------begin report---------------")

    for char in keys:

        print(f"The '{char}' character appears {charCount[char]} times.")

    print("----end report----")


main()









