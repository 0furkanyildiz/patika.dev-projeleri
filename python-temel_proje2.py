"""2. Sorunnun Açıklaması:

Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]"""


def upside_down(l1):
    l2 = l1[::-1]

    for i in range(len(l2)):
        if len(l2[i]) > 1:
            l2[i] = l2[i][::-1]

    return l2

l1 = [[1, 2], [3, 4], [5, 6, 7]]

print(upside_down(l1))