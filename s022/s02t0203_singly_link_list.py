# Importando la clase nodo desde el archivo s02t0101_linked_list.py
from s02t0201_linked_list import Node

# Creando la clase de una lista enlazada
class SinglyLinkedList:

    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Metodo de insercion de Nodo en la lista
    def append(self, data):
        # Se crea un nuevo nodo
        new_node = Node(data)

        # Si hay un tail, el nuevo nodo pasa a ser el nuevo tail
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node 
        # Si no hay tail
        else:
            self.talil = new_node
            self.head = new_node
        # Se incrementa size en 1
        self.size += 1
        
    # Insertando en posicion intermedia
    # [A -> B -> C] -1 3
    # [o 1 2]
    # size = 3
    def append_at_location(self, data, index):
        if index < 1 or index > self.size + 1:
            raise IndexError(f"Indice {index} fuera de rango")

        # Crear un nuevo nodo
        new_node = Node(data)

        # Insertar al inicio de la lista
        if index == 1:
            new_node.next = self.head
            self.head = new_node
            if self.tail == None:
                self.tail = new_node
            # Incremento en 1 el tamaño
            self.size += 1
            # Creando variables de control para las inseciones intermedias
            current = self.head
            preview = None
            position = 1

            # Traversal (Recorrido)
            while current is not None and position < index:
                preview = current
                current = current.next
                position += 1

            #Llegando a la posicion
            if current is None:
                preview.next = new_node
                self.tail = new_node
                self.size += 1
                return

            # Si se llega a una posicion intermedia
            #TOOO
# Se crea la funcion principal
def main():
    # Creando una instancia de una lista enlazada
    my_list = SinglyLinkedList()
    # Agregando elementos a la lista
    my_list.append(30)
    my_list.append(59)
    my_list.append(80)
    my_list.append(100)

    # Recorrer la lista
    for value in my_list.head.iter():
        print(f"{value}, ", end=" ")
    print()


if __name__ == "__main__":
    main()


