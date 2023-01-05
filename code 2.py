# -*- coding: utf-8 -*-

from pro1_8 import Rectangle, Cercle, Triangle, Carre, TriangleRectangle, GeoFig, tout_perimetre, tout_superficie, decris_toi  
if __name__ == '__main__':
    try:
        Rec = Rectangle("Rectangle RT1", 10, 5)
        Cer = Cercle("Cercle CL1", 8)
        Tri = Triangle("Triangle TR1", 4, 8, 12)
        Car = Carre("Carré A4", 6)
        Tri_rec = TriangleRectangle("Triangle Rectangle TRRT 1", 1, 9)
        
        print()
        print("Le polymorphisme\n")
        decris_toi(Rec)
        print()
        decris_toi(Cer)
        print()
        decris_toi(Tri)
        print()
        decris_toi(Car)
        print()
        decris_toi(Tri_rec)
        print()
        
    except Exception:
        print("Données non pris en charge.")