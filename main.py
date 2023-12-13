meret: int= 40
jel = "*"
szokoz= " "
penz: int = 0
elet: int = 5
kulcs : int = 0
helyszinek: int = 0
if elet == 0:
    print("MEGHALTÁL!")

import design

design.kinezet(jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, "Karakterlap", jel, meret)
design.karakterlap(jel, "Erő", elet, jel, meret)
design.karakterlap(jel, "Pénz", penz, jel, meret)
design.karakterlap(jel, "Kulcs", kulcs, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.kinezet(jel, meret)






design.kinezet(jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, "Kamra", jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.kinezet(jel, meret)

design.kinezet(jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, "Ajtó", jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.kinezet(jel, meret)

design.kinezet(jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, "Vártemplom (szerzetes)", jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.kinezet(jel, meret)

design.kinezet(jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, "Faajtó", jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.kinezet(jel, meret)

design.kinezet(jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, "NYERTÉL!", jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.kinezet(jel, meret)




print ("Utad során különböző helyszínekre kerülsz, ahonnan szabadon átmehetsz másik helyszínre, a megadott módon. Akár ide-oda is mászkálhatsz, bár ennek meglesz a következménye, ld: technikai leírásnál! Az adott helyszínen megvizsgálhatsz tárgyakat, fel is veheted őket vagy akár használhatod őket. Ha egy helyszínen felvettél egy tárgyat, akkor az legközelebb már nincs ott! Ha felvettél egy tárgyat, akkor és csak akkor van lehetőséged használni, ha erre kiadod a megfelelő parancsot. Ez lehet a kulcsa a továbbjutásnak. Amennyiben rossz helyen használsz egy tárgyat, akkor az a tárgy nem veszik el, csak nem történik változás a történet menetében.")

print("Az életerő: A harmadik helyszínváltás után elkezd csökkeni az életerő, helyszínenként eggyel! Erről tájékoztatni kell a játékost! Kezdetben az életereje 5, ha talál ételt és megeszi (használja), akkor ismét 3 helyszínváltásig nem csökken, és maximumomra (10) kerül. Majd újra elkezd csökkenni helyszínenként eggyel. Ha nullára csökken, akkor vége a játéknak, nincs erőnk továbbmenni…")




enter = input("A játék kezdéséhez nyomjon egy ENTER-t!")

design.kinezet(jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, "Mező", jel, meret)
design.karakterlap(jel, "Erő", elet, jel, meret)
design.karakterlap(jel, "Pénz", penz, jel, meret)
design.karakterlap(jel, "Kulcs", kulcs, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.kinezet(jel, meret)
epulet: str = str(input("Egy óriási mezőn vagy. Nyugat felé egy hatalmas épület körvonalai tűnnek fel."))
if "megy epulet" in epulet:
    print("Elindultál az épület felé!")
    helyszinek += 1

design.kinezet(jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, "Mező", jel, meret)
design.karakterlap(jel, "Erő", elet, jel, meret)
design.karakterlap(jel, "Pénz", penz, jel, meret)
design.karakterlap(jel, "Kulcs", kulcs, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.kinezet(jel, meret)



mezo: str = str(input("Napfényes mezőn állsz. Nyugatra egy hatalmas kastélyt, délre egy kutat látsz."))
if "megy del" in mezo:
    if elet == 0:
        print("MEGHALTÁL!")
    design.kinezet(jel, meret)
    design.jel_kiiras(jel, szokoz, jel, meret)
    design.jel_kiiras(jel, szokoz, jel, meret)
    design.jel_kiiras(jel, "Kút", jel, meret)
    design.karakterlap(jel, "Erő", elet, jel, meret)
    design.karakterlap(jel, "Pénz", penz, jel, meret)
    design.karakterlap(jel, "Kulcs", kulcs, jel, meret)
    design.jel_kiiras(jel, szokoz, jel, meret)
    design.jel_kiiras(jel, szokoz, jel, meret)
    design.kinezet(jel, meret)
    print("Napfényes mezőn állsz, egy kút előtt. Itt van: pénz. Nyugatra egy hatalmas kastéyt látsz.")
    helyszinek += 1
    penz_felvetel: str = str(input("Felveszed a pénzt?"))
    if "felvesz" in penz_felvetel:
        penz += 1
        print("Felvetted a pénzt!")
        epulet1: str = str(input("Egy óriási mezőn vagy. Nyugat felé egy hatalmas épület körvonalai tűnnek fel."))
        if "megy epulet" in epulet1:
            helyszinek += 1
            if helyszinek == 3:
                elet -= 1
            if elet == 0:
                print("MEGHALTÁL!")
            design.kinezet(jel, meret)
            design.jel_kiiras(jel, szokoz, jel, meret)
            design.jel_kiiras(jel, szokoz, jel, meret)
            design.jel_kiiras(jel, "Kastély", jel, meret)
            design.karakterlap(jel, "Erő", elet, jel, meret)
            design.karakterlap(jel, "Pénz", penz, jel, meret)
            design.karakterlap(jel, "Kulcs", kulcs, jel, meret)
            design.jel_kiiras(jel, szokoz, jel, meret)
            design.jel_kiiras(jel, szokoz, jel, meret)
            design.kinezet(jel, meret)
            print("Elindultál a kastély felé!")
        else: 
            ujra: str = str("Rossz parancsot adott meg! Adja meg ujra: ")

varudvar: str = str(input("A várudvaron állsz. Nyugatra nyitott kamrát, északra zárt ajtót látsz. Egy széles lépcő vezet fel a vártemplomhoz."))
if "megy vartemplom" in varudvar:
    helyszinek += 1
    if helyszinek >= 3:
        elet -= 1
    if elet == 0:
        print("MEGHALTÁL!")
    design.kinezet(jel, meret)
    design.jel_kiiras(jel, szokoz, jel, meret)
    design.jel_kiiras(jel, szokoz, jel, meret)
    design.jel_kiiras(jel, "Vártemplom (szerzetes)", jel, meret)
    design.karakterlap(jel, "Erő", elet, jel, meret)
    design.karakterlap(jel, "Pénz", penz, jel, meret)
    design.karakterlap(jel, "Kulcs", kulcs, jel, meret)
    design.jel_kiiras(jel, szokoz, jel, meret)
    design.jel_kiiras(jel, szokoz, jel, meret)
    design.kinezet(jel, meret)
    print("A templom előtt egy kéregető szerzetes mosolyog rád. Nyugatra nyitott kamrát, északra zárt ajtót látsz.")
    kulcs_vetel: str = str(input("Van lehetőség kulcsot felvenni a szerzetestől, de ez 1 pénzbe kerül. "))
    if "felvesz" in kulcs_vetel:
        penz -= 1
        kulcs += 1
        print("Megvetted a kulcsot a szerzetestől!")
        visszafele: str = str(input("Az utad a kastélyba vezet vissza."))
        if "megy epulet" in visszafele:
            helyszinek += 1
            if helyszinek >= 3:
                elet -= 1
            if elet == 0:
                print("MEGHALTÁL!")
            design.kinezet(jel, meret)
            design.jel_kiiras(jel, szokoz, jel, meret)
            design.jel_kiiras(jel, szokoz, jel, meret)
            design.jel_kiiras(jel, "Kastély", jel, meret)
            design.karakterlap(jel, "Erő", elet, jel, meret)
            design.karakterlap(jel, "Pénz", penz, jel, meret)
            design.karakterlap(jel, "Kulcs", kulcs, jel, meret)
            design.jel_kiiras(jel, szokoz, jel, meret)
            design.jel_kiiras(jel, szokoz, jel, meret)
            design.kinezet(jel, meret)
valasztasok: str = str(input("Mehetsz a kamra és az ajtó felé. "))
if "megy ajto" in valasztasok:
    helyszinek += 1
    if helyszinek >= 3:
        elet -= 1
    if elet == 0:
        print("MEGHALTÁL!")
    design.kinezet(jel, meret)
    design.jel_kiiras(jel, szokoz, jel, meret)
    design.jel_kiiras(jel, szokoz, jel, meret)
    design.jel_kiiras(jel, "Ajtó", jel, meret)
    design.karakterlap(jel, "Erő", elet, jel, meret)
    design.karakterlap(jel, "Pénz", penz, jel, meret)
    design.karakterlap(jel, "Kulcs", kulcs, jel, meret)
    design.jel_kiiras(jel, szokoz, jel, meret)
    design.jel_kiiras(jel, szokoz, jel, meret)
    design.kinezet(jel, meret)
    visszafelee: str = str(input("Ezt az ajtót nem lehet semmivel sem kinyitni! Csak a kastély fele mehetsz!"))
    if "megy epulet" in visszafele:
            helyszinek += 1
            if helyszinek >= 3:
                elet -= 1
            if elet == 0:
                print("MEGHALTÁL!")
            design.kinezet(jel, meret)
            design.jel_kiiras(jel, szokoz, jel, meret)
            design.jel_kiiras(jel, szokoz, jel, meret)
            design.jel_kiiras(jel, "Kastély", jel, meret)
            design.karakterlap(jel, "Erő", elet, jel, meret)
            design.karakterlap(jel, "Pénz", penz, jel, meret)
            design.karakterlap(jel, "Kulcs", kulcs, jel, meret)
            design.jel_kiiras(jel, szokoz, jel, meret)
            design.jel_kiiras(jel, szokoz, jel, meret)
            design.kinezet(jel, meret)
    valasztasok: str = str(input("Mehetsz a kamra és az ajtó felé. "))


elif "megy kamra" in valasztasok: 
    kajak: str = str(input("Rengeteg ételt látsz a kamrában. Veszel fel ételt? "))
    if "felvesz" in kajak:
        helyszinek += 1
        elet == 10
        design.kinezet(jel, meret)
        design.jel_kiiras(jel, szokoz, jel, meret)
        design.jel_kiiras(jel, szokoz, jel, meret)
        design.jel_kiiras(jel, "Kamra", jel, meret)
        design.karakterlap(jel, "Erő", elet, jel, meret)
        design.karakterlap(jel, "Pénz", penz, jel, meret)
        design.karakterlap(jel, "Kulcs", kulcs, jel, meret)
        design.jel_kiiras(jel, szokoz, jel, meret)
        design.jel_kiiras(jel, szokoz, jel, meret)
        design.kinezet(jel, meret)
        kamra: str = str (input("A kamrában vagy. Egyik oldalon hatalmas asztal áll mindenféle ételekkel, a másik oldalon egy nagy tűzhely, szintén ételekkel. Délre egy faajtót látsz."))
        if "megy faajto" in kamra and kulcs == 1:
            nyeres: str = str(input("Használod a kulcsot? (Igen/Nem)"))
            if "Igen" or "Nem" in nyeres:
                design.kinezet(jel, meret)
                design.jel_kiiras(jel, szokoz, jel, meret)
                design.jel_kiiras(jel, szokoz, jel, meret)
                design.jel_kiiras(jel, "NYERTÉL!", jel, meret)
                design.jel_kiiras(jel, szokoz, jel, meret)
                design.jel_kiiras(jel, szokoz, jel, meret)
                design.kinezet(jel, meret)


    


    




