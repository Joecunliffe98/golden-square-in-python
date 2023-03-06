
def check_punctuation(string):
    if not isinstance(string, str):
        raise Exception("Invalid Input - Not a String")
    
    suitable_endings = ".!?"

    if (string[0].isupper()) & (string[-1] in suitable_endings):
        return True
    elif (string[0].isupper()):
        return "You didn't close the sentence!"
    elif (string[-1] in suitable_endings):
        return "You forgot your capital letter!"
    else:
        return "You forgot your capital letter, and your sentence does not close!"