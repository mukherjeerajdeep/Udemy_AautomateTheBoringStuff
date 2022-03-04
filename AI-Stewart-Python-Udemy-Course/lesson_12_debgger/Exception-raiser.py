'''

**************
*            *
*            *
*            *
**************

'''

def boxPrint(symbol, width, height):
    if len(symbol) != 1 :
        raise Exception('"symbol" should be a string with lenght 1.')
    if (width < 2) or (height <2):
        raise Exception('"width and height" should be a string with lenght 2.')
    
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width-2)) + symbol)

    print(symbol * width)


boxPrint('*', 1, 1)
        
