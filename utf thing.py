def binarytodecimal(binary):
    length = len(binary) - 1
    total = 0
    for i in binary:
        if i == "1":
            total +=(2**length)
        else:
            total+=(0)
        length = length -1
    return total
            
def decimaltobinary(decimal):
    decimal = int(decimal)
    binary = ""
    while decimal != 0:
        binary = str(decimal %2) + binary
        decimal //= 2
    return binary

def convertchartobin(s):
    bins = []
    utf = ''
    for x in s:
        x = ord(x)
        x = decimaltobinary(x)
        bins.append(x)
    for b in bins:
        b = '0' + b
        utf = utf + b
    return utf

def convertbintochar(s):
    
        
    