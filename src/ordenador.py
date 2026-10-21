class Ordenador:
    def bubble_sort(self, vet):
        n = len(vet)
        for i in range(n, 1, -1):        
            for j in range(0, i - 1):    
                if vet[j] > vet[j + 1]:
                    aux = vet[j]
                    vet[j] = vet[j + 1]
                    vet[j + 1] = aux
        return vet
    