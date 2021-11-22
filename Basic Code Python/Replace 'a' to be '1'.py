def main():
    kata = str(input("Masukkan kata yang mengandung a: "))
    replace_result = "".join(kata.replace('a' , '1')) 
    print("String with replaced Content : " , replace_result) 
    
if __name__ == '__main__':
    main()