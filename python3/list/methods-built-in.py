
List = [1,2,3,4]

def objek():
    return 1

# append() menambahkan item / objek ke dalam list
List.append(objek)
print (List)

# count() mengembalikan jumlah berapa kali objek terjadi didalam list
print (List.count(objek))

# extend() menambahkan isi sequence ke list (iterable item )
List.extend(["ina"] * 5)
print(List)

# index() : mengembalikan indeks terendah dalam list yang muncul obj
# menampilkan indeks sebelum objek yang dimasukan kedalam index()
List.insert(1,objek)
print (List)
print (List.index(objek))

# pop() Menghapus dan mengembalikan objek atau obj terakhir dari list
List.pop(1)
print (List)

# remove () menghapus objek dari list
def y():
    return "y"

List.insert(1,y)
print (List)
List.remove(objek)
List.remove(y)
print (List)

#reverse() membalikan list objek ditempat
List.reverse()
print (List)


# sort()  Urutkan objek list, gunakan compare func jika diberikan
del List
List = [a for a in range(10)]
List.reverse()
print (List)
List.sort()
print (List)
