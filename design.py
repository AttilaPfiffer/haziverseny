def kinezet(jel, meret):
    print(jel*meret)
    
def jel_kiiras(jel, szokoz, jel2, meret):
    hossz: int = int(meret-(len(jel) + len(jel2)))
    print(f"{jel}{szokoz:^{hossz}}{jel2}")

def hely_kiiras(jel, hely, jel2, meret):
    hossz: int = int(meret-(len(jel) + len(jel2)))
    print(f"{jel}{hely:^{hossz}}{jel2}")

def karakterlap(jel, szoveg, db, jel2, meret):
    behuzas1 = meret-5
    behuzas2 = int(meret/11)
    print(f"{jel}{szoveg:<{behuzas1}}{db:<{behuzas2}}{jel2}")
