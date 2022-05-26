# Check if two words are anagrams 
# Example:
# find_anagram("hello", "check") --> False
# find_anagram("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = list(word)
    word.sort()
    
    anagram = list(anagram)
    anagram.sort()
    
    result = word == anagram
    
    return result
    
    
def read_file_content(filename):
    with open(filename) as doc:
        lines = doc.readlines()
    
    return lines


def count_words():
    count_dictionary = {}
    text = read_file_content("./story.txt")

    for line in text:
        for word in line.split():
            if word.lower() in count_dictionary:
                count_dictionary[word] += 1
            else:
                count_dictionary[word.lower()] = 1
    
    return count_dictionary
