# Se crea una lista de estudiantes
students_list_01 = ['Juan', 'Pedro', 'Maria', 'Jose']  # O(1)

def random_function(students):
    first = students[0]  # O(1)
    total = 0  # O(1)
    new_list = []  # O(1)

    for student in students:  
        total += 1  # O(n)
        new_list.append(student)  # O(n)
        
    print(new_list)  # O(1) para una sola impresión
    return total  # O(1)

print(random_function(students_list_01))  