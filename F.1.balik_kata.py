''' mengubah kalimat = 'Hai aku Lintang' menjadi 'iaH uka gnatniL' '''

teks = input('Ketik kalimat: ')
def BaliKata(teks):
    hasil = []
    kalimat = teks.split(' ')
    for kata in kalimat:
        hasil.append(kata[::-1])
    hasil = ' '.join(hasil)
    return hasil
print(BaliKata(teks))
