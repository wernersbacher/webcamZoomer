
def convertTuples(lis):

    tuple_list = []

    for elem in lis:
        if isinstance(elem, list):
            t = convertTuples(elem)
            tuple_list.append(t)
        else:
            tuple_list.append(elem)

    return tuple(tuple_list)
