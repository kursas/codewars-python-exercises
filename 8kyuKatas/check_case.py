#write a function that will check if two given chaaracters are the same case.
#if any of characters is not a letter return -1
#if both characters are the same case,return 1
#if both characters are ltters and not the same case,return 0
#for example:
# "a"and "f"return 1
#"b" and "G"return 0
#"\t" and "Z"return -1
def same_case(a,b):
    if not a.isalpha() or not b.isalpha():
        return -1
    if a.isupper() == b.isupper():
        return 1
    else:
        return 0
print(f"padavem A ir ? grazino:{same_case('A','?')}")

def same_case2(a,b):
    return a.isupper()==b.isupper if a.isalpha() and b.isalpha() else -1
print(f"padavem A ir ? grazino:{same_case2('A','?')}")

def same_case3(a,b):
    return -1*(not(a+b).isalpha()) or not a.islower()^b.islower()
print(f"padavem A ir ? grazino:{same_case2('A','?')}")

#output
padavem A ir ? grazino:-1
padavem A ir ? grazino:-1
padavem A ir ? grazino:-1

Process finished with exit code 0
