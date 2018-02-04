'''Important to note if the string is ASCII or Unicode. 
Return false if the string length is > 128 since that's the max number of unique char.
'''
# my solution
def is_unique_string(input_string):
    index = 1
    for character in input_string:
        for next_character in input_string[index:]:
            if character == next_character:
                return False
                break
        index += 1
    return True

# suggested solution
def is_unique_string_2(input_string):
    if len(input_string) > 128:
        return False
    char_set = set()
    for character in input_string:
        if character in char_set:
            return False
            break
        char_set.add(character)
    return True
        

print (is_unique_string("helo"))
print (is_unique_string("hello"))

print (is_unique_string_2("helo"))
print (is_unique_string_2("hello"))