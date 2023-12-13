meret: int= 40
jel = "*"
szokoz= " "
penz: int = 0

import design

design.kinezet(jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, "Mező", jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.kinezet(jel, meret)

design.kinezet(jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, "Kút", jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.kinezet(jel, meret)

design.kinezet(jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, "Kastély", jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
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
design.jel_kiiras(jel, "Ajó", jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.kinezet(jel, meret)

design.kinezet(jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, "Szerzetes", jel, meret)
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
design.jel_kiiras(jel, "Épület", jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.jel_kiiras(jel, szokoz, jel, meret)
design.kinezet(jel, meret)
epulet: str = str(input("Egy óriási mezőn vagy. Nyugat felé egy hatalmas épület körvonalai tűnnek fel."))
if "megy epulet" or "Megy epulet" or "megy épület" or "Megy épület" in epulet:
    print("Elindultál az épület felé!")
mezo: str = str(input("Napfényes mezőz állsz. Nyugatra egy hatalmas kastélyt, délre egy kutat látsz."))
if "megy kut" or "Megy kut" or "megy kút" or "Megy kút":
    print("Napfényes mezőn állsz, egy kút előtt. Itt van: pénz. Nyugatra egy hatalmas kastéyt látsz.")
    penz += 1



