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
        
        # Si la lista esta vacia, el nuevo nodo se convierte en la cabeza
        if not self.head:
            self.head = new_node
            return

        # Si la lista no esta vacia, se recorre hasta el final y se agrega el nuevo nodo
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # Insertando en posicion intermedia
    def append_at_location(self, data, index):
        if index < 0

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


