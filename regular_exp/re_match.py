import re

pattern = '^a...s'

def re_match(pattern):
    test_string = 'abyss'
    result = re.match(pattern, test_string)
    if result:
        print('Search successfull')
    else:
        print('Search unuccessfull')

re_match(pattern)