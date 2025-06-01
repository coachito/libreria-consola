import time
import datetime
import csv
import os
archivo_csv = "libreria.csv"
lista_libreria = []
def display_menu(opciones):
    print("""
Bienvenido a la librería Ortegon!
En esta librería encontrarás diferentes opciones para realizar y revisar.
También puedes guardar tus libros y gestionarlos.

¿Qué aventura haremos hoy?
""")
    for i, o in enumerate(opciones, start=1):
        print(f"{i}. {o}")

def cargardesdecsv():
    if os.path.exists(archivo_csv):
        with open(archivo_csv, mode="r", newline="",encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for file in lector:
                lista_libreria.append(file)
                print(f"Datos cargados correctamente desde {archivo_csv}")
    else:
        print(f"No existe el archivo {archivo_csv} este se creará cuando guardes tu primer libro")

def guardarcsv():
    with open(archivo_csv, mode="w", newline="",encoding="utf-8") as f:
        campos = ["Nombre", "Autor", "Año", "Leido"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for libro in lista_libreria:
            escritor.writerow(libro)
    print(f"Se acaba de guardar en {archivo_csv}") 


def eliminar():
    try:
        while True:
            nombre = input("¿Cuál es el nombre del libro que deseas buscar?:\n")
            coincidencias = [l for l in lista_libreria if nombre.lower() in l["Nombre"].lower()]
            if coincidencias:
                print(f"\nSe encontraron {len(coincidencias)} coincidencias para '{nombre}':")
                for i, libro in enumerate(coincidencias, start=1):
                    print(f"{i}. Libro: {libro['Nombre']}\nAutor: {libro['Autor']}\nAño: {libro['Año']}")
                while True:
                    try:
                        opcion_eliminar = int(input("\n¿Qué libro vas a eliminar? (número): ")) - 1
                        eliminar_libro = coincidencias[opcion_eliminar]
                        lista_libreria.remove(eliminar_libro)
                        print(f"El libro '{eliminar_libro['Nombre']}' ha sido eliminado correctamente.")
                        guardarcsv()
                        termina = input(f"¿Vas a eliminar otro libro asociado a '{nombre}'? (s/n):\n")
                        if termina.lower() == "n":
                            break
                    except (ValueError, IndexError):
                        print("No has seleccionado un índice válido.")
            else:
                print("No se encontraron coincidencias.")
            term = input("¿Quieres eliminar otro libro? (s/n):\n")
            if term.lower() == "n":
                break
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def buscar():
    try:
        while True:
            nombre = input("Ingrese el nombre del libro a buscar: \n")
            coincidencias = [t for t in lista_libreria if nombre.lower() in t["Nombre"].lower()]
            if coincidencias:
                print(f"\nSe encontraron {len(coincidencias)} coincidencias:\n")
                for i, l in enumerate(coincidencias, start=1):
                    print(f"{i}. Libro: {l['Nombre']}, Autor: {l['Autor']}, Año: {l['Año']} ¿Leído?: {l['Leido']}")
                    time.sleep(1)
            else:
                print("No se encontraron coincidencias.")
            termina = input("\n¿Buscar otro libro? (s/n): ")
            if termina.lower() == "n":
                break
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def crear():
    while True:
        try:
            nombre = input("¿Cuál es el nombre del libro a agregar?: \n")
            autor = input("¿Quién es el autor del libro?: \n")
            año = input("¿Cuál es el año del libro a ingresar? (YYYY): \n")
            leido = input("¿Ya lo leíste? (si/no): \n").strip().lower()
            diccionario = {
                "Nombre": nombre,
                "Autor": autor,
                "Año": año,
                "Leido": leido
            }
            lista_libreria.append(diccionario)
            print(f"\nEl libro '{nombre}' de {autor} ha sido añadido correctamente.")
            guardarcsv()
            continuar = input("¿Quieres seguir añadiendo libros? (s/n):\n")
            if continuar.lower() == "n":
                break
        except Exception as e:
            print(f"Error al crear libro: {e}")

def listar_año():
    try:
        lista_ordenada = sorted(lista_libreria, key=lambda e: datetime.datetime.strptime(e["Año"], "%Y"))
        print("\nLa lista ha sido ordenada por año:")
        for i, p in enumerate(lista_ordenada, start=1):
            print(f"{i}. Nombre: {p['Nombre']}, Autor: {p['Autor']}, Año: {p['Año']} ¿Leído?: {p['Leido']}")
            time.sleep(1)
    except Exception as e:
        print(f"Error al ordenar por año: {e}")

def listar_autor():
    lista_ordenada = sorted(lista_libreria, key=lambda e: e["Autor"].lower())
    print("\nLa lista ha sido ordenada por autor:")
    for i, p in enumerate(lista_ordenada, start=1):
        print(f"{i}. Nombre: {p['Nombre']}, Autor: {p['Autor']}, Año: {p['Año']} ¿Leído?: {p['Leido']}")
        time.sleep(1)

def listar_leidos():
    try:
        while True:
            print("1) Listar leídos\n2) Listar no leídos")
            opcion = input("¿Qué libros quieres buscar? (1-2): ")
            if opcion == "1":
                estado = "si"
            elif opcion == "2":
                estado = "no"
            else:
                print("Opción inválida.")
                continue
            ordenado = [t for t in lista_libreria if t["Leido"].lower() == estado]
            print()
            for i, p in enumerate(ordenado, start=1):
                print(f"{i}. Nombre: {p['Nombre']}, Año: {p['Año']}, Autor: {p['Autor']}, Leído: {p['Leido']}")
                time.sleep(1)
            break
    except Exception as e:
        print(f"Error al listar libros: {e}")

def main():
    cargardesdecsv()
    try:
        while True:
            display_menu([
                "Agregar Libro",
                "Buscar Libro por título",
                "Eliminar libro por título",
                "Listar todos los libros",
                "Listar libros leídos o no leídos",
                "Salir"
            ])
            try:
                opcion = int(input("\nElige una opción (1-6): "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if opcion == 1:
                crear()
            elif opcion == 2:
                buscar()
            elif opcion == 3:
                eliminar()
            elif opcion == 4:
                while True:
                    print("1) Listar por Año\n2) Listar por Autor")
                    c = input("¿Cómo quieres listar los libros? (1-2):\n")
                    if c == "1":
                        listar_año()
                        break
                    elif c == "2":
                        listar_autor()
                        break
                    else:
                        print("Opción inválida.")
            elif opcion == 5:
                listar_leidos()
            elif opcion == 6:
                print("¡Gracias por usar la librería Ortegon! Hasta la próxima.")
                break
            else:
                print("Elige una opción entre 1 y 6.")
    except Exception as e:
        print(f"Ocurrió un error general: {e}")

if __name__ == "__main__":
    main()

        