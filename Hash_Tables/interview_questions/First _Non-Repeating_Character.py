# HT: First Non-Repeating Character ( ** Interview Question)
# You have been given a string of lowercase letters.

# Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return None.

# For example, if the input string is "leetcode", the function should return "l" because "l" is the first character that appears only once in the string. Similarly, if the input string is "hello", the function should return "h" because "h" is the first non-repeating character in the string.

# WRITE THE FUNCTION HERE #
def first_non_repeating_char(string):
    str_counts = {}
    for letter in string:
        str_counts[letter] = str_counts.get(letter, 0) + 1 
 
 
    for letter, count in str_counts.items():
        if count == 1:
            return letter
    return None
    
###########################



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""