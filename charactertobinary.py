
def chartobinary(word_input):
    def decimaltobinary(decimal):
        decimal = int(decimal)
        binary = ""
        while decimal != 0:
            binary = str(decimal %2) + binary
            decimal //= 2
        return binary

    def convertchar(wrd):
        for x in wrd:
            deci = []
            deci.append(ord(x))
        return deci

    
    outpt = convertchar(word_input)

    for x in outpt:
        print(decimaltobinary(x))
        
        

print(chartobinary('20ac'))