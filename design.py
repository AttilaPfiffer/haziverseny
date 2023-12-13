def kinezet(jel, meret):
    print(jel*meret)
    
def jel_kiiras(jel,szokoz, jel2, meret):
    hossz: int = int(meret-(len(jel) + len(jel2)))
    print(f"{jel}{szokoz:^{hossz}}{jel2}")

def hely_kiiras(jel, hely, jel2, meret):
    hossz: int = int(meret-(len(jel) + len(jel2)))
    print(f"{jel}{hely:^{hossz}}{jel2}")