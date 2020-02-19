# Dit is gewoon een makkelijk functie om een tuple om te zetten naar een int
def tuple_to_int(tpl):
    lst = []
    for i in tpl:
        lst.append(str(i))
    return int(list_to_string(lst))


# Een functie die ik nodig heb voor een tuple naar int te zetten
def list_to_string(lst):
    str1 = ''
    return str1.join(lst)


# Een functie om een string om te zetten naar een list
def string_to_list(str1):
    strLst = ['x'] * 4
    for i in range(0, len(str1)):
        strLst[i] = str1[i]

    return strLst


# Een functie om een integer om te zetten naar een list
def int_to_list(lst):
    strings = [str(item) for item in lst]
    return int("".join(strings))