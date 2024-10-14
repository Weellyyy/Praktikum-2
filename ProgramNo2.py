def angkaterbesar (a, b, c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
        
num1 = float(input("Masukkan angka pertama: "))
num2 = float(input("Masukkan angka kedua: "))
num3 = float(input("Masukkan angka ketiga: "))

terbesar = angkaterbesar(num1, num2, num3)


print(f"Angka terbesar adalah: {terbesar}")
    
    