from xmlrpc.client import boolean


def addnum (a,b):
    if type(a) == type(b) == type(1):
        return a+b
    else:
        return ("sorry!, enter integer number")
result = addnum(5,5)
print(result)    