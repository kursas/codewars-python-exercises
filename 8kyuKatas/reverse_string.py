#complete the solution so that it reverses the string passed into it.
def solution(string):
    result_string=''
    for i in range(len(string)-1,-1,-1):
        result_string += string[i]
    return result_string
print(f"hallo world- paakeite i:{solution('hallo world')}")

def solution1(str):
    return str[::-1]
print(f"labas rytas- paakeite i:{solution1('labas rytas')}")

def solution3(string):
    newstring=''
    letter=len(string)-1
    for x in string:
        x=string[letter]
        newstring=newstring+x
        letter=letter-1
    return newstring
print(f"labas rytas, štai ir aš- paakeite i:{solution3('labas rytas, štai ir aš')}")

#output
hallo world- paakeite i:dlrow ollah
labas rytas- paakeite i:satyr sabal
labas rytas, štai ir aš- paakeite i:ša ri iatš ,satyr sabal

Process finished with exit code 0
