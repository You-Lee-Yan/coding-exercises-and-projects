'''In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )'''

def alphabet_position(text):
    letter_alph_positions = ""
    for char in text.lower() :
        if(char.isalpha()) :
            letter_alph_positions += str(ord(char) - ord('a') + 1) + " "
    return letter_alph_positions[:-1]

def alphabet_position_v2 (text):
    return " ".join(str(ord(char) - ord('a') + 1) for char in filter(lambda char: char.isalpha(), text.lower()))

#alphabet_position_v3() isn't my solution
def alphabet_position_v3(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


