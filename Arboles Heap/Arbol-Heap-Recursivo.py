import sys

class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.front = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return pos * 2

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        return pos * 2 > self.size

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    #Funcion para amontonar el nodo en una posicion dada y de manera recursiva
    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            left = self.leftChild(pos)
            right = self.rightChild(pos)
            smallest = pos
        
        # Encuentra el hijo más pequeño
            if left <= self.size and self.Heap[left] < self.Heap[smallest]:
                smallest = left
            if right <= self.size and self.Heap[right] < self.Heap[smallest]:
                smallest = right

            if smallest != pos:
                self.swap(pos, smallest)
                self.minHeapify(smallest) #Llamamos a la recursividad

    #Funcion para insertar en el heap un nodo (Aqui inicia el proceso recursivo)
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
        self.insert_recursive(self.size)

    #Funcion auxiliar reccursiva para ajustar el heap luego de haber insertado
    def insert_recursive(self, current):
        if current > 1 and self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            self.insert_recursive(self.parent(current)) #LLamada recursiva

    # Función para mostrar el heap
    def Print(self): 
        for i in range(1, (self.size // 2) + 1): 
            print(f" Nodo Padre: {self.Heap[i]} \nHijo Izquierdo: {self.Heap[2 * i]} \nHijo Derecho: {self.Heap[2 * i + 1]}") 

    # Función para construir el heap mínimo utilizando minHeapify
    def minHeap(self): 
        for pos in range(self.size // 2, 0, -1): 
            self.minHeapify(pos) 

    #Funcion para borrar y devolver el elemento min del heap, este utiliza recursividad a traves de "minHeapify"
    def remove(self):
        popped = self.Heap[self.front]
        self.Heap[self.front] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.front) #Llama a la funcion minHeapify recursivamente
        return popped

# Menú interactivo para el heap
if __name__ == "__main__":
    heap = MinHeap(15)

    while True:
        print("\nMenú:")
        print("1. Insertar elemento")
        print("2. Mostrar heap")
        print("3. Eliminar elemento")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            element = int(input("Ingrese el elemento a insertar: "))
            heap.insert(element)
        elif opcion == "2":
            heap.Print()
        elif opcion == "3":
            if heap.size == 0:
                print("El heap está vacío. No hay elementos para eliminar.")
            else:
                print("Elemento eliminado:", heap.remove())
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")