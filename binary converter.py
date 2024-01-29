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

    
    
    
        
        

    
    


choice = input("Would you like to...\n(A) Convert Binary to Decimal Numbers\n(B) Convert Decimal to Binary Numbers\n)
if choice == "a" or "A":
    binaryString = input('Enter a Binary Number: ')
    print(binarytodecimal(binaryString))

if choice == "b" or "B":
    inputDecimal = input('Enter a Decimal number: ')
    print(decimaltobinary(inputDecimal))


    
    

    







