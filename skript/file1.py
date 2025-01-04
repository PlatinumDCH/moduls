from collections import Counter

def get_vowels(String):
    return [each for each in String if each in 'aeiou']

def capitalize(String):
    return String.title()

def merge(dict1, dict2):
    dict3 = dict1 | dict2
    return dict3

def anagram(first, second):
    return Counter(first) == Counter(second)

