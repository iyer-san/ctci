def character_replace(input_string):
    result_string = []
    for character in input_string:
        if(character == " "):
            result_string.append("20%")
        else:
            result_string.append(character)
    return ''.join((result_string))

print (character_replace("hello hello"))

#in place implementation
def char_replace(input_char):
    if(input_char == " "):
         return "20%"
    else:
        return input_char
input_string = "hello fellow"
a =  "".join(char_replace(character) for character in input_string)
print (a)
