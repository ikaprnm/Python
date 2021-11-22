def balik_kata(input):
    a = input
    r1 = "".join(reversed(a))
    b = r1.split()
    r2 = " ".join(reversed(b))
    c = r2.swapcase()
    return c

if __name__ == '__main__':
    input = str(input("Masukkan nama Anda: "))
    print (balik_kata(input))
