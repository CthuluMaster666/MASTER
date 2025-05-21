

class Abbility_Points():

    def getpunkty(self,poziomtrudnosci):
        punktyumiejetnosci=0
        if poziomtrudnosci == "łatwy":
            punktyumiejetnosci = 75
        elif poziomtrudnosci == "sredni":
            punktyumiejetnosci = 50
        elif poziomtrudnosci == "trudny":
            punktyumiejetnosci = 25
        return punktyumiejetnosci

p=Abbility_Points()
punkty=p.getpunkty("łatwy")
print(punkty)
punkty=p.getpunkty("sredni")
print(punkty)
punkty=p.getpunkty("trudny")
print(punkty)