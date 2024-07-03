import os

def main():
    # i = 1
    mulai_nomor = int(input("Mulai dari nomor berapa?"))    # ini buat kalo mulai lagi dari 201, 401, dst
    nama_file = input("Nama filenya nanti apa?")            # ini bebas, pokoknya ngikut buat semua

    path = "D:\\tung\\python\\rename\\ADV"
    for filename in os.listdir(path):
        my_dest = nama_file + str(mulai_nomor) + ".png"
        my_source = path + "/" + filename
        my_dest = path + "/" + my_dest
        os.rename(my_source, my_dest)
        mulai_nomor += 1
    
# print("Gambar sudah diurutkan")    
if __name__ == '__main__':
    main()
