# -*- coding: utf-8 -*-
from pro1_7 import Rectangle, Cercle, Triangle, Carre, TriangleRectangle, GeoFig  
if __name__ == '__main__':
    print("Depuis les classes qui sont seules :")
    print()
    try:
        Rec = Rectangle("Rectangle RT1", 10, 5)
        Cer = Cercle("Cercle CL1", 8)
        Tri = Triangle("Triangle TR1", 4, 8, 12)
        Car = Carre("Carré CR1", 5)
        Tri_rec = TriangleRectangle("Triangle Rectangle TRRT 1", 1, 9)
        
        Rec.decris_toi()
        print()
        Cer.decris_toi()
        print()
        Tri.decris_toi()
        print()
        Car.decris_toi()
        print()
        Tri_rec.decris_toi()
        print()
    except Exception:
        print("Données non pris en charge.")
    
    print()
    print()
    print("Depuis la classe Générale : ")
    print()
    fig1 = GeoFig() 
    fig2 = GeoFig() 
    fig3 = GeoFig()
    fig4 = GeoFig()
    fig5 = GeoFig()
    
    fig1.add(Rectangle("Rectangle RT2", 15, 8))
    fig2.add(Cercle("Cercle CL2", 6))
    fig3.add(Triangle("Triangle TR2", 10, 12, 14))
    fig4.add(Carre("Carré CR2", 20))
    fig5.add(TriangleRectangle("Triangle Rectangle TRRT 2", 5, 7))
    
    fig1.decris_toi()
    fig2.decris_toi()
    fig3.decris_toi()
    fig4.decris_toi()
    fig5.decris_toi()
    
    try:
        pass

    except Exception:
        print("Donnnées non pris en charge.")        


