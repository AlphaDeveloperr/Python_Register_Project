from time import sleep

id = 1
          
class Register():
    
    
    def __init__(self):
        self.persons = {"Isim" : [], "E-posta" : [], "Yas" : [], "Id" : []}

    def singin(self):
        print("------------Kayit_Yap------------")
        self.name = input("İsminiz: ")
        self.email = input("E-postaniz: ")
        self.age = input("Yasiniz: ")
        print("---------------------------------")
        sleep(1)
    
    def add(self):
        self.persons["Isim"].append(self.name)
        self.persons["E-posta"].append(self.email)
        self.persons["Yas"].append(self.age)
        self.persons["Id"].append(id)
        print(f"Kaydiniz yapilmistir. Id'niz {id}'dir")
        sleep(1)
    
    def log(self):
        print("-----------Veri_Tabani-----------")
        for i,j in self.persons.items():
            print(f"{i} = {j}")
        print("---------------------------------")
        sleep(1)
        
    def login(self):
        print("------------Giris_Yap------------")
        self.jrname = input("İsminiz: ")
        self.jremail = input("E-postaniz: ")
        if (self.jrname in self.persons["Isim"]) and (self.jremail in self.persons["E-posta"]):
            print("Giris basarili!")
        else:
            print("Basarisiz giris tekrar deneyiniz!")
            self.login()
        print("---------------------------------")
        sleep(1)
        
    def writeindata(self):
        with open("database.txt","w") as file:
            for i,j in self.persons.items():
                file.write(f"{i} = {j}\n")
        with open("database.txt","r") as file:
            file.read()
        
    def delete(self):
        if len(self.persons["Id"]) == 0:
            print("Veri tabaninda hic veri bulunamamktadir!")
            print("---------------------------------")
        else:
            self.del_id = int(input("Silmek istediginiz hesabin Id'sini giriniz: "))
            if self.del_id in self.persons["Id"]:
                x = self.persons["Id"].index(self.del_id)
                for k,l in self.persons.items():
                    l.pop(x)
                print("Hesap silinmistir!")
                print("---------------------------------")
                sleep(1)
            else:
                print("Bu Id'ye ait hesap bulunmamaktadir, tekrar deneyiniz!")
                sleep(1)
                self.delete()
    
    def search(self):
        if len(self.persons["Id"]) == 0:
            print("Veri tabaninda hic veri bulunamamktadir!")
            print("---------------------------------")
        else:
            self.search_id = int(input("Id'nizi giriniz: "))
            if self.search_id in self.persons["Id"]:
                print("----------Bilgileriniz----------")
                x = self.persons["Id"].index(self.search_id)
                for i,j in self.persons.items():
                    print(f"{i} = {j[x]}")
                print("---------------------------------")
                sleep(1)
            else:
                print("Bu Id'ye ait hesap bulunmamaktadir, tekrar deneyiniz!")
                sleep(1)
                self.search()


        

        
r = Register()   

        
while True:
    
    print("----------Islemler----------\n1.Kayit Yap\n2.Giris Yap\n3.Id Sorgula\n4.Veri Tabani Sorgula\n5.Kayit Sil\n6.Cikis Yap")
    
    secim = int(input("Yapacaginiz islemi numarasina gore seciniz: "))
    sleep(1)
    
    if secim == 1:
        r.singin()
        r.add()
        r.writeindata()
        id += 1
        continue
    elif secim == 2:
        r.login()
        continue
    elif secim == 3:
        r.search()
        continue
    elif secim == 4:
        r.log()
        continue
    elif secim == 5:
        r.delete()
        r.writeindata()
        continue
    elif secim == 6:
        print("Cikis yapiliyor...")
        sleep(2)
        print("Iyi Gunler!")
        break
    else:
        print("Gecersiz islem tekrar deneyiniz!")
        continue