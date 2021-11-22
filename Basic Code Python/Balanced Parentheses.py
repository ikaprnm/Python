def check(input):
    symbol = ['()', '{}', '[]']
    while any(x in input for x in symbol):
        for sym in symbol:
            input = input.replace(sym, '')
    return not input
   
if __name__ == "__main__":
    input = "[{(())}]"
    print(input, "-", "Balanced" 
        if check(input) else "Unbalanced")