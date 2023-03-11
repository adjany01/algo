from Module_classe_fonctions import*

ArrQueue=ArrayQueue()
for i in range(4):
    ArrQueue.enqueue(i*4-1)
    
    print("La taille du tableau est: ",ArrQueue.__len__())
print()
ArrStack=ArrayStack()
ArrStack.push(2)
ArrStack.push(8)
ArrStack.push("travail")
ArrStack.top()
print("La taille est: ",ArrStack.__len__())
print()
x= DynamicArray()
print("Le tableau actuel possede {} elements et une capacite elementaire de {}".format(x._n, x._capacity))
#On peut définir alors une nouvelle liste  de 30 elements
for i in range(30):
    x.append(i)
print("Ce nouveau tableau possède {} elements et une capacité de {}".format(len(x), x._capacity))
# En se servant de __getitem__ on cherche la position d'un element dans notre tableau
    
print("L'element qui occupe la position 15 est: {}".format(x.__getitem__(16)))
    
    # Puisque notre tableau possede 30 élément avec une capacité de 32
    # Dans ce cas si nous ajoutons 1'élément c'est seulement les nombres d'élément qui changer et non la capacité
x.append(107)
print("Le nombre d'élément du tableau est", x._n,"mais la capacité est toujours égale à", x._capacity )
    # Notre capacité devrait double si on ajoute deux autres elements
x.append(0)
x.append(5)
print("Le nombre d'élément du tableau est", x._n,"Mais la capacité devient égale à", x._capacity )
    #Essayons avec un tableau ayant una capacité de 
x._resize(35)
print("Le nombre d'élément du tableau est {} et  la capacité devient égale à {}".format(x._n,x._capacity))
    #On crée un tableau avec une capacité quelconque
y = x._make_array(10)
print(y)
print()
LStack=LinkedStack()
for i in range(4):
    LStack.push(i)
    print("la taille de la pile est, pour chaque iteration:", LStack.__len__()," et l'element en tete est, ",LStack.top())

print()
Linkedqueue=LinkedQueue()
Linkedqueue.enqueue(4)
Linkedqueue.enqueue(6)
Linkedqueue.enqueue(6)
Linkedqueue.enqueue(1)

print("La taille de notre linkedQueue est ",Linkedqueue.__len__())