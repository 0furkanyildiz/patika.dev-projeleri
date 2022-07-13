"""1. Sorunun Açıklaması:

Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]"""

a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def func(liste):
    for i in range(len(liste)):
        if type(liste[i]) == list:
            for b in range(len(liste[i])):
                liste.insert(i,liste[i][b])
                i += 1
            liste.remove(liste[i])

    for i in liste:
        if type(i) == list:
            func(liste)
    return liste

print(func(a))