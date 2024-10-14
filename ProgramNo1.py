def evaluatestudent(persen):
    if persen >= 90:
        print ("Excellent performance")
    elif persen >= 80:
        print ("Very Good performance")
    elif persen >= 70:
        print ("Good performance")
    elif persen >= 60:
        print ("average performance")
    else:
        print("Sampai Jumpa di Semester Antara")
        
persen = int(input("Masukkan Nilai: "))
nilai = evaluatestudent(persen)
    
