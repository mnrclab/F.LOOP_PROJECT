#SOAL PERTAMA
list = ['1', '2', '3', '4', '5']
isi = ''
for i in list:
    isi += ' '+str(i)+' '
    print(isi)

#SOAL KEDUA
list = ['1', '2', '3', '4', '5']
list.reverse()
isi = ''
for i in list:
    isi += ' '+str(i)+' '
    print(isi)

#SOAL KETIGA
for i in range(0, 5):
    print((str(i+1) + ' ') *(i+1))

#SOAL KEEMPAT
for i in range(0, 5):
    print((str(i+1) + ' ') *(5-i))

#SOAL KELIMA
for i in range(0, 1):
    a = ['1', '2', '3', '4', '5']
    b = str(a[4])
    print(b)
    b += ' ' + str(a[3])
    print(b)
    b += ' ' + str(a[2])
    print(b)
    b += ' ' + str(a[1])
    print(b)
    b += ' ' + str(a[0])
    print(b)

#SOAL KEENAM
for i in range(0, 1):
    a = str(5) + ' ' + str(4) + ' ' + str(3) + ' ' + str(2) + ' ' + str(1)
    print(a)
    for j in range(0, 1):
        b = str(5) + ' ' + str(4) + ' ' + str(3) + ' ' + str(2)
        print(b)
        for k in range(0, 1):
            c = str(5) + ' ' + str(4) + ' ' + str(3)
            print(c)
            for l in range(0, 1):
                d = str(5) + ' ' + str(4)
                print(d)
                for m in range(0, 1):
                    e = str(5)
                    print(e)
