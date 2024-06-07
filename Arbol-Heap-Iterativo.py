# Existen dos tipos de códigos Heap en programación, el MaxHeap y el
# MinHeap. En este caso, analizaremos el código MinHeap.
# Fuente: https://www.geeksforgeeks.org/min-heap-in-python/?ref=ml_lbp

import sys 

class MinHeap: 

	def __init__(self, maxsize): 
		self.maxsize = maxsize 
		self.size = 0
		self.Heap = [0]*(self.maxsize + 1) 
		self.Heap[0] = -1 * sys.maxsize 
		self.FRONT = 1

	# Función para devolver la posición de 
    # padre para el nodo actualmente 
    # en la posición
	def parent(self, pos): 
		return pos//2

	# Función para devolver la posición de 
	# el hijo izquierdo del nodo actualmente 
	# en la posición
	def leftChild(self, pos): 
		return 2 * pos 

	# Función para devolver la posición de 
	# el hijo adecuado para el nodo actualmente 
	# en la posición
	def rightChild(self, pos): 
		return (2 * pos) + 1

	# Función que devuelve verdadero si se pasa 
	# el nodo es un nodo hoja 
	def isLeaf(self, pos): 
		return pos*2 > self.size 

	# Función para intercambiar dos nodos del heap 
	def swap(self, fpos, spos): 
		self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 

	#Función para amontonar el nodo en pos 
	def minHeapify(self, pos): 

		# Si el nodo es un nodo no hoja y mayor 
		# que cualquiera de sus hijos
		if not self.isLeaf(pos): 
			if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
			self.Heap[pos] > self.Heap[self.rightChild(pos)]): 

				# Intercambiar con el hijo izquierdo y amontonar 
				# el hijo izquierdo
				if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
					self.swap(pos, self.leftChild(pos)) 
					self.minHeapify(self.leftChild(pos)) 

				# Intercambiar con el hijo adecuado y amontonar 
				# el hijo correcto 
				else: 
					self.swap(pos, self.rightChild(pos)) 
					self.minHeapify(self.rightChild(pos)) 

	# Función para insertar un nodo en el montón
	def insert(self, element): 
		if self.size >= self.maxsize : 
			return
		self.size+= 1
		self.Heap[self.size] = element 

		current = self.size 

		while self.Heap[current] < self.Heap[self.parent(current)]: 
			self.swap(current, self.parent(current)) 
			current = self.parent(current) 

	# Función para mostrar el heap 
	def Print(self): 
		for i in range(1, (self.size//2)+1): 
			print(" Nodo Padre: "+ str(self.Heap[i])+" \nHijo Izquierdo: "+
								str(self.Heap[2 * i])+" \nHijo Derecho: "+
								str(self.Heap[2 * i + 1])) 

	# Función para construir el montón mínimo usando 
	# la función minHeapify 
	def minHeap(self): 

		for pos in range(self.size//2, 0, -1): 
			self.minHeapify(pos) 

	# Función para eliminar y devolver el mínimo
	# elemento del montón 
	def remove(self): 

		popped = self.Heap[self.FRONT] 
		self.Heap[self.FRONT] = self.Heap[self.size] 
		self.size-= 1
		self.minHeapify(self.FRONT) 
		return popped 

# Vamos a añadir un menú interactivo
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
