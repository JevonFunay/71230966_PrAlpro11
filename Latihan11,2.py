data = ('Jevon Christian Putra Funay', '71230966', 'Tegalrejo,DI Yogyakarta')
print("Data : ",data)

namalengkap, nim, alamat = data
print("NIM      : ", nim)
print("NAMA     : ", namalengkap)
print("ALAMAT   : ", alamat)

nim2 = tuple(nim)
namadepan = tuple(namalengkap.split()[0].lower())
namabalik = tuple(reversed(namalengkap.split()))
print("NIM          : ", nim2)
print("NAMA DEPAN   : ", namadepan)
print("NAMA TERBALIK: ", namabalik)
