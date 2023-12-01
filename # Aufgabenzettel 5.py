# Aufgabenzettel 5 
# Paul Gnädig, Tim Duske
# Tutorium Di 8-10 Uhr C.Roschek

#Aufgabe 1b


# binäre_suche(list[int], k):
# Voraussetzung: Liste ist aufsteigend sortiert
# Ergebnis: die kleinste Zahl dre Liste größer als k ist geliefert, wenn k nicht in xs ist, dann ist die länge von xs geliefert.
# Effekt:
'''Tests:
1. binäre_suche([1,2,3,4,5,6,7,8,9], 5) == 5
2. binäre_suche([],5) == 0
3. binäre_suche ([3,45,67,89,99,1000], 89) == 4

'''



# def binary_search(xs, k):
#     n = len(xs)
#     # This function searches k in xs in the range left to right-1
#     def bin_search(left, right):
#         if left >= right: # k is not in xs
#             return n
#         m_pos = (left + right) // 2 # index of the element in the middle
#         m = xs[m_pos] # element in the middle
#         if k == m: # k has been found
#             return m_pos + 1
#         elif k < m: # search in left half
#             return bin_search(left, m_pos)
#         else: # m < k # search in right half
#             return bin_search(m_pos + 1, right)
#         # invocation of the help function
#     return bin_search(0, n)

# print(binary_search([1,2,3,4,5,6,7,8,42,67,130], 8))



# Aufgabe 1c

# insertionsort(List[int]): 
# Voraussetzug: keine
# Ergebnis: die Eingabeliste ist aufsteigend sortiert
# Effekt: keiner
''' Tests:
1. insertionsort([8,-8,6,5,353,1,2,4,59]) == [-8,1,2,4,5,6,8,59,353]
2. insertionsort([]) == 0
3. insertionsoert([0]) == [0]
'''



def binary_search(xs, k):       # definition für insertionsort
    n = len(xs)
    if n == 0:
        return 0
    # This function searches k in xs in the range left to right-1
    def bin_search(left, right):
        if left >= right: # k is not in xs
            return n
        m_pos = (left + right) // 2 # index of the element in the middle
        m = xs[m_pos] # element in the middle
        if n <= 1 and m<k:
            return 1
        if m < k and xs[m_pos+1] > k:
            return m_pos + 1
        elif m > k and xs[m_pos-1] < k:
            return m_pos
        if k == m: # k has been found
            return m_pos + 1
        elif k < m: # search in left half
            return bin_search(left, m_pos)
        else: # m < k # search in right half
            return bin_search(m_pos + 1, right)
        # invocation of the help function
    return bin_search(0, n)




def insert(xs, i):
    key = xs[i]
    j = i
    ys = xs[:i]
    p = binary_search(ys,key)
    while j >= p:
        xs[j] = xs[j-1]
        j -= 1 
    xs[p] = key
    print(xs)

def insertion_sort(xs):
    n = len(xs)
    # insert the elements step by step in the sorted front part
    for i in range(1,n-1):
        insert(xs, i)
    return xs




# # Funktionen für Aufgabe 1d


# def mergesort(xs):          
#     n = len(xs)
#     if n <= 1:
#         return
#     left = xs[:n//2]        # Liste mit allen Elementen der linken Hälfte
#     right = xs[n//2:]       # alle Elemente der rechten Liste

#     mergesort(right)        # ist left un right leer?
#     mergesort(left)         # ist left und right leer?
    
#     merge(left, right , xs)     # hilsfunktion wird aufgerufen
#     print(xs)
    


# def merge(left, right, xs):         # Hilsfunktion
#     l = 0
#     r = 0
#     while l + r < len(xs):
#         if l == len(left):
#             xs[l + r] = right[r]
#             r += 1
#         elif r == len(right):
#             xs[l + r] = left[l]
#             l += 1
#         elif left[l] <= right[r]:
#             xs[l + r] = left[l]
#             l += 1
#         else:
#             xs[l + r] = right[r]
#             r += 1
    



# def insert(xs, i):    # Hilfsfunktion
#     key = xs[i]
#     j = i
#     while(j > 0 and xs[j-1] > key):
#         xs[j] = xs[j-1]
#         j -= 1
#     xs[j] = key 


# def insertion_sort(xs):
#     n = len(xs)
#     for i in range (1, n):
#         insert(xs,i)


# # Aufgabe 1d

# # powersort(xs) :
# # Voraussetzung: keine
# # Ergebnis: die liste ist aufsteigend sortiert
# # Effekt: sortierte Liste ist auf dem Bildschirm ausgegeben 
# '''Tests:
# 1. powersort([15,2,1,0,-5]) == [-5,0,1,2,15]
# 2. powersort ([0]) == [0]
# 3. powersort([4.4,54,11,-15,-25]) == [-25,-15,4.4,11,54]
# '''

    

# def powersort(xs):
#     if len(xs) == 1:        # wenn x nur ein Eleemnet hat wir xs augegeben 
#         return xs
#     n = len(xs)
#     erste = xs[:n//3]           # erste teilliste beinhaltete das erste drittel von xs
#     zweite = xs[n//3:((n//3)*2)]    # zweite Teilliste beinhaltet das zweite drittel von xs
#     dritte = xs[n//3*2:n]           # dritte Teilliste beinhaltet das letzte drittel von xs
#     insertion_sort(erste)           # Anwendung von Insertionsort auf eins und drei (siehe Zeile 108)
#     insertion_sort(dritte)
#     if len(xs) >= 1:
#         powersort(zweite)               # rekrusionschritt auf zweite Teilliste
#     mergesort(erste + zweite + dritte)    # mergen der einzelnen Teillisten zu einer sortierten
    
    

# #Aufgabe 2a siehe PDF

# #Aufgabe 2b siehe PDF


# #Aufgabe 2c


# # quick_sort(List[ys]) :
# # Voraussetzung: Die Elemente von xs liegen in einem total geordnetem Universum
# # Ergebnis: die Liste xs ist aufsteigend sortiert
# Effekt: keiner
'''Tests:
1. quicksort([7,0,-1,99,1228,1,2,13]) == [-1,0,1,2,7,13,99,1228]
2. quciksort([]) == 0
'''


def quick_sort(ys):
    # This help function sorts the elements in xs between
    # start (inclusive) and end (exclusive)
    xs = []
    for i in range(0, len(ys)):    #für i länge der Liste
        tup = (ys[i],i)            # erstelle Tupel mit Wert und index der eingabeliste
        xs.append(tup)              # füge die Tuple in die leere Liste

    def quicksort_help(start, end):
        if (end-start <=1): # Recursion anchor
            return
            
        # The splitting part:
        pivot = xs[start]
        l = start
        for i in range(start+1,end):
            if xs[i] < pivot:
                l = l+1
                xs[i], xs[l] = xs[l], xs[i]
        xs[start], xs[l] = xs[l], xs[start]
        # l is now the index of the pivot element
        
        # Sort the two remaining lists recursively.
        quicksort_help(start, l)
        quicksort_help(l+1, end)
    quicksort_help(0, len(ys))
    zs=[]
    for i in range(0,len(xs)):  # für alle Tupel in xs
        zs.append(xs[i][0])     # füge die Tupel jeweils ur mit dem ersten Element in zs ein.
    return zs


print(quick_sort([3,5,2,15,23,1,2]))

# Das neue Quicksortverfahren ist stabil, weil jedem Tupel ein zweiter Eindeutiger Index zugewiesen wird, wodurch bei der
# lexikographischen Ordnung die Reihenfolge gleicher Elemente beachtet wird.


# Aufgabe 2d

# # megasort(List[xs]) :
# # Voraussetzung: Die Elemente von xs liegen in einem total geordnetem Universum
# # Ergebnis: die Liste xs ist aufsteigend sortiert
# Effekt: keiner
'''Tests:
1. megasort([7,0,-1,99,1228,1,2,13]) == [-1,0,1,2,7,13,99,1228]
2. megasort([])
'''

import random

def megasort(xs):
    # This help function sorts the elements in xs between
    # start (inclusive) and end (exclusive)
    def quicksort_help(start, end):
        if (end-start <=1): # Recursion anchor
            return
            
        # The splitting part:
        pivot1 = random.randint(start,end-1)
        pivot2 = random.randint(start,end-1)
        while pivot2 == pivot1:
            pivot2 = random.randint(start,end-1)
        pivot3 = random.randint(start,end-1)
        while pivot3 == pivot1 or pivot3 == pivot2:
            pivot3 = random.randint(start,end-1)

        if xs[pivot1] > xs[pivot2] and xs[pivot1] < xs[pivot3]:
            global pivot
            pivot = xs[pivot1]
        elif xs[pivot1] > xs[pivot3] and xs[pivot1] < xs[pivot2]:
            pivot = xs[pivot1]
        if xs[pivot2] > xs[pivot1] and xs[pivot2] < xs[pivot3]:
            pivot= xs[pivot2]
        elif xs[pivot2] > xs[pivot3] and xs[pivot2] < xs[pivot1]:
            pivot = xs[pivot2]
        if xs[pivot3] > xs[pivot1] and xs[pivot3] <xs[pivot2]:
            pivot= xs[pivot3]
        elif xs[pivot3] > xs[pivot2] and xs[pivot3] < xs[pivot1]:
            pivot = xs[pivot3]
        if pivot==xs[pivot1]:
            j = pivot1
            for x in range(0, j+1):
                xs[j]=xs[j-1]
                j -=1
            xs[0]=pivot
        elif pivot==xs[pivot2]:
            j = pivot2
            for x in range(0, j+1):
                xs[j]=xs[j-1]
                j -=1
            xs[0]=pivot
        else:
            j = pivot3
            for x in range(0, j+1):
                xs[j]=xs[j-1]
                j -=1
            xs[0]=pivot


        l = start
        for i in range(start+1,end):
            if xs[i] < pivot:
                l = l+1
                xs[i], xs[l] = xs[l], xs[i]
        xs[start], xs[l] = xs[l], xs[start]
        # l is now the index of the pivot element
        
        # Sort the two remaining lists recursively.
        quicksort_help(start, l)
        quicksort_help(l+1, end)
    quicksort_help(0, len(xs))
    print(xs)

print(megasort([2,4,12,5,1,78,42]))



