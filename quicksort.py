from pilha import Pilha

class Quicksort:

    def __init__ (self):
        self.pilha = Pilha()

    def dividir(self,arr,l,h):
        i = ( l - 1 )
        x = arr[h]
        for j in range(l , h):
            if arr[j] <= x:
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[h] = arr[h],arr[i+1]
        return (i+1)


    # lista[] --> Array to be sorted,
    # l  --> Starting index,
    # h  --> Ending index

    def quickSortIterative(self,lista,l = 0,h = 0):
        self.pilha.push(l)
        self.pilha.push(h)
        while self.pilha.pilha_nao_vazia():
            h = self.pilha.pop_pilha()
            l = self.pilha.pop_pilha()

            p = self.dividir( lista, l, h )

            if p-1 > l:
                self.pilha.push(l)
                self.pilha.push( p - 1 )
            if p+1 < h:
                self.pilha.push( p + 1 )
                self.pilha.push( h )


arr = [4, 3, 5, 2, 1, 3, 2, 3]
n = len(arr)
print (n)
a = Quicksort()
a.quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i])
