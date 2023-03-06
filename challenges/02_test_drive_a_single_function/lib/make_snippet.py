def make_snippet(string):
    list1 = string.split()
    if len(list1) > 5:
        list1 = list1[:5]
        list1 = " ".join(list1)
        sentence = list1 + "..."
    else:
        list1 = list1[:(len(list1))]
        sentence = " ".join(list1)
    return sentence