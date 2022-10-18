class kreditka:
    
    def cislo_uctu(self, predcisli, cislo, kod = "1278"):
        if len(predcisli) == 6 and len(cislo) == 9:
            c_uctu = predcisli + "-" + cislo + "/" + kod
            print("\nČíslo účtu:", c_uctu)
        else:
            print("\nČíslo účtu:", "Špatný formát čísla účtu")
      
    def pin(self, pin = 7887):
        print("PIN:", pin)
    
    def udaje(self, jmeno, prijmeni, trida):
        print(jmeno, prijmeni, trida)
    
    def vypis(self):
        banka.cislo_uctu(predcisli, cislo)
        banka.pin()
        banka.udaje(jmeno, prijmeni, trida)


  
predcisli = input("Zadejte předčíslí: ")
cislo = input("Zadejte číslo: ")
jmeno = input("Zadejte křestní jméno: ")
prijmeni = input("Zadejte příjmení: ")
trida = input("Zadejte třídu: ")     

banka = kreditka() 
banka.vypis()       
