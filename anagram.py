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
    

