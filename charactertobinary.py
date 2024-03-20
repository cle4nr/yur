
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
        
    
'''
binary_out = chartobinary('20ac') 
while len(binary_out) < 8:
    binary_out = '0' + binary_out
    
'''