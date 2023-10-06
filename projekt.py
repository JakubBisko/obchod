ZelenýLesník = 200
GreenCycle = 500  
EkoFlow = 180

OmegaZen = 850
HerbalHarmony = 1099
SuperBoost = 500

Aquawarrior = 300
EthicalWear = 1800
VeganStyle = 4400

nakup = []

print("\nVítejte v EkoOáze\n")

kosik = 0

while True:

    print("1)Ekologické domácí potřeby   2)Zdravá výživa   3)Udržitelná móda")

    uzivatel = input("Zadejte číslo sekce: ")

    if uzivatel == '1':

        print("\n1)Zelený Lesník - Ekologický mycí gel")

        print("2)GreenCycle - Nádoby na separovaný sběr bioodpadu")

        print("3)EkoFlow - Biologické menstruační vložky\n")

        uzivatel = input("Zadejte číslo produktu: ")

 

        if uzivatel == '1':

            kosik += ZelenýLesník  

            print("Zelený Lesník za 200 CZK.")

            nakup.append("ZelenýLesník")


        elif uzivatel == '2':

            kosik += GreenCycle  

            print("GreenCycle za 500 CZK.")

            nakup.append("GreenCycle")

 

        elif uzivatel == '3':

            kosik += EkoFlow  

            print("EkoFlow za 180 CZK.")

            nakup.append("EkoFlow")  

 

        elif uzivatel not in ['1', '2', '3']:

            print("neplatná hodnota")


    elif uzivatel == '2':

        print("\n1)OmegaZen - Čaj s marihuanou (příchuť vody)")

        print("2)HerbalHarmony -  Bylinné extrakty(především z marihuany) pro podporu imunity")

        print("3)SuperBoost - Chia semínka, spirulina a acai berry(od guru Mr.Jsoky)\n")

        uzivatel = input("Zadejte číslo produktu: ")


        if uzivatel == '1':

            kosik += OmegaZen  

            print("OmegaZen za 850 CZK.")

            nakup.append("OmegaZen")


        elif uzivatel == '2':

            kosik += HerbalHarmony  

            print("HerbalHarmony za 1099 CZK.")

            nakup.append("HerbalHarmony")


        elif uzivatel == '3':

            kosik += SuperBoost  

            print("SuperBoost za 500 CZK.")

            nakup.append("SuperBoost")  


        elif uzivatel not in ['1', '2', '3']:

            print("neplatná hodnota")      


    elif uzivatel == '3':

        print("\n1)Aquawarrior - láhev na vodu ekologická k životnímu prostředí(rozpustná ve vodě)")

        print("2)EthicalWear -  kalhoty z recyklovaných materiálů(jako jsou plasty, sklo a injekční stříkačky)")

        print("3)VeganStyle - Vegan kabelky z umělé kůže\n")

        uzivatel = input("Zadejte číslo produktu: ")

        if uzivatel == '1':

            kosik += Aquawarrior  

            print("Aquawarrior za 300 CZK.")

            nakup.append("Aquawarrior")


        elif uzivatel == '2':

            kosik += EthicalWear  

            print("EthicalWear za 1800 CZK.")

            nakup.append("EthicalWear")

        elif uzivatel == '3':

            kosik += VeganStyle  

            print("VeganStyle za 4400 CZK.")

            nakup.append("VeganStyle")


    elif uzivatel not in ['1', '2', '3']:

        print("neplatná hodnota")


    volba = input("\nChcete pokračovat (ano/ne)? \n")

    if volba.lower() == 'ne':

        print(f"\nCelková cena v košíku: {kosik} CZK")

        print("Zakoupené produkty:")

        for polozka in nakup:

            print(polozka)

        break