# function will convert string parameter to upper case
def to_upper(text):
    # Task6
    if isinstance(text, str) == False:
        raise TypeError("this is wrong")
    return text.upper()

# function will check return true if all items on
# the parameter list are upper case
def to_word_list_isupper(str_list):
    # Task6
    if isinstance(str_list, list) == False:
        raise TypeError("this is wrong")
    for word in str_list:
        if word.islower():
            return False
    return True