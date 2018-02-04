# decide if a string is permutation of the other
'''
Check if the strings are case sensitive. Is whitespace significant?
Alternate solution could be to count the count each char occurs in each of the strings ad see if they match.
'''

def check_permutation(first_string, second_string):
    if (len(first_string) == len(second_string)):
        a = ''.join(sorted(first_string))
        b = ''.join(sorted(second_string))
        return (a == b)
    else:
        return False
print (check_permutation("hello", "ohell"))
print (check_permutation("hello", "yohell"))