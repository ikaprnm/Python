def ConvertDecToBinary(dec):
    if dec>=1:
        ConvertDecToBinary(dec//2)
        print(dec%2, end = "")
if __name__ == "__main__":
    dec = int(input("Input Decimal:"))
    ConvertDecToBinary(dec)
    print()