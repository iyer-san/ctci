def string_rotate(input_string, comparison_string):

    if not len(input_string) == len(comparison_string):
        return False
    first_character = input_string[0]
    first_index = comparison_string.index(first_character)
    result_string = (comparison_string[first_index:] + comparison_string[:first_index])
    boolean_result = (result_string == input_string)
    return boolean_result

print (string_rotate("hello", "elloh"))